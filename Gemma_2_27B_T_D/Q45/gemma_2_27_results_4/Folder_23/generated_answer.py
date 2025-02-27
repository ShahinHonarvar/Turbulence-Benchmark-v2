from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[0:7] if c.isalpha())).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 4 and ''.join(p) == ''.join(p)[::-1]}