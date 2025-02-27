from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    perms = set((''.join(p) for p in permutations(letters)))
    palindromes = set((p for p in perms if len(p) >= 4 and p == p[::-1]))
    return palindromes