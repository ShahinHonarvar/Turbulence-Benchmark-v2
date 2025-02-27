from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    return {''.join(p) for p in permutations(s) if len(p) >= 5 and p == p[::-1]}