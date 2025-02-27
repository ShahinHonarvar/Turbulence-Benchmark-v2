import itertools

def palindromes_between_indices(s):
    subset = [c for c in s[:6] if c.isalpha()]
    perms = set((''.join(p) for r in range(5, len(subset) + 1) for p in itertools.permutations(subset, r)))
    return {p for p in perms if p.lower() == p.lower()[::-1]}