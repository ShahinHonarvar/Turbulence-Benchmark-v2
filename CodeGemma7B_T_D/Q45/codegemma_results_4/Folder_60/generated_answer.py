from itertools import permutations

def palindromes_between_indices(s):
    return {''.join(p) for p in permutations(s[3:7].lower()) if len(p) >= 4}