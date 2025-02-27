from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:9] if c.isalpha()]
    letters = [c.lower() for c in letters]
    perms = permutations(letters)
    palindromes = set((p for p in perms if p == p[::-1] and len(p) >= 4))
    return palindromes