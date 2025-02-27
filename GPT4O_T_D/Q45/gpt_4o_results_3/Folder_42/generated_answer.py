from itertools import permutations

def palindromes_between_indices(s: str):
    if len(s) < 10:
        return set()
    substring = s[6:10].lower()
    english_letters = [c for c in substring if c.isalpha()]
    if len(english_letters) < 3:
        return set()

    def is_palindrome(st):
        return st == st[::-1]
    results = set()
    for length in range(3, len(english_letters) + 1):
        for perm in set(permutations(english_letters, length)):
            joined_perm = ''.join(perm)
            if is_palindrome(joined_perm):
                results.add(joined_perm)
    return results