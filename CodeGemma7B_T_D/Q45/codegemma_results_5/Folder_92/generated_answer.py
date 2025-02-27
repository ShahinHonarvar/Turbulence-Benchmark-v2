from itertools import permutations

def palindromes_between_indices(s):
    return {''.join(p) for p in permutations(sorted([c.lower() for c in s[4:8]])) if len(p) >= 4}