from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[3:8] if c.isalpha())).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 6 and p == p[::-1]}