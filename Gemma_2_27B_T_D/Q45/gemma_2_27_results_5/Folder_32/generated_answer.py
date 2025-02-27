from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted([c for c in s[1:8] if c.isalpha()]))
    return set((p.lower() for p in (''.join(perm) for perm in permutations(letters)) if len(p) >= 5 and p.lower() == p.lower()[::-1]))