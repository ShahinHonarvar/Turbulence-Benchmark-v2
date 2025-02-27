from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[1:8] if c.isalpha()]
    all_perms = set((''.join(p).lower() for i in range(6, len(letters) + 1) for p in permutations(letters, i)))
    return {p for p in all_perms if is_palindrome(p) and len(p) >= 6}