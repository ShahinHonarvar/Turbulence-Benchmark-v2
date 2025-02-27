from itertools import permutations

def palindromes_between_indices(s):
    return {''.join(p) for p in permutations(s[4:8].lower()) if p == p[::-1] and len(p) >= 4} or set()