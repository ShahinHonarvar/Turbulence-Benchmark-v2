from itertools import product

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    return {''.join(p) for p in product(*[l.lower() for l in s[4:8]] * 4) if p in english_letters}