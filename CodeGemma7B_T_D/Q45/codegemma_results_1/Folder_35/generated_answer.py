from itertools import permutations

def palindromes_between_indices(s):
    p = permutations((c.lower() for c in s[2:5]), 4)
    return {''.join(d) for d in p if d == d[::-1]}