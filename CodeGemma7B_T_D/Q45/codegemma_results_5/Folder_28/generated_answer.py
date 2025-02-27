from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[1:6] if c.isalpha()]
    return {''.join(p) for p in permutations(letters) if len(p) >= 4}