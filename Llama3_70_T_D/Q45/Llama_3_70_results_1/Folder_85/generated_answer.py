from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    return {''.join(p) for r in range(7, len(letters) + 1) for p in permutations(letters, r) if p == p[::-1]}