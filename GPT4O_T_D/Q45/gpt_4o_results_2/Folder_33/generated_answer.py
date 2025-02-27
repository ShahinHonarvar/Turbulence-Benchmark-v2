from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[7:10].lower()

    def is_palindrome(perm):
        counter = Counter(perm)
        odd_count = sum((1 for count in counter.values() if count % 2 != 0))
        return odd_count <= 1

    def create_palindrome(half):
        if len(half) % 2 == 0:
            return half + half[::-1]
        else:
            return half + half[-2::-1]
    results = set()
    char_count = Counter((c for c in substring if c.isalpha()))
    half_size = sum(char_count.values()) // 2
    half_permutations = (p for p in permutations(char_count.elements(), half_size))
    for half in half_permutations:
        if is_palindrome(half):
            palindrome = create_palindrome(half)
            if len(palindrome) >= 4:
                results.add(palindrome)
    return results