from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()

    def is_palindrome(word):
        lw = word.lower()
        return lw == lw[::-1]
    subset = ''.join([char.lower() for char in s[1:8] if char.isalpha()])
    results = set()
    for length in range(5, len(subset) + 1):
        for perm in permutations(subset, length):
            p = ''.join(perm)
            if is_palindrome(p):
                results.add(p)
    return results