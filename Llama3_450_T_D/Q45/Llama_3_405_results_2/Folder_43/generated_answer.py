from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(p):
        return p == p[::-1]
    letters = [c for c in s[2:6] if c.isalpha()]
    perms = set((''.join(p) for r in range(4, len(letters) + 1) for p in permutations(letters, r)))
    return set((p for p in perms if is_palindrome(p.casefold())))