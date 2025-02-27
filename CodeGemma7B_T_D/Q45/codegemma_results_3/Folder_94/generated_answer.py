from itertools import permutations

def palindromes_between_indices(s):
    english = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    if not s[3:5]:
        return set()
    perms = permutations(s[3:5])
    return {''.join(p) for p in perms if p == p[::-1]}