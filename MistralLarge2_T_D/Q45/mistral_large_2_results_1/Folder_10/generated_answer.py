from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[:6] if c.isalpha()]
    perm = set((''.join(p) for p in permutations(letters, len(letters)) if is_palindrome(p) and len(p) >= 3))
    return {p.lower() for p in perm}