from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[:3].lower() if c.isalpha()]
    return set((p for p in [''.join(perm) for perm in permutations(letters)] if p == p[::-1] and len(p) >= 3))