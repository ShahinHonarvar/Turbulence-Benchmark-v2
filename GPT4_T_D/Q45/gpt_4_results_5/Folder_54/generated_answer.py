from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10]
    s = ''.join(filter(str.isalpha, s)).lower()
    perms = set([''.join(p) for p in permutations(s) if len(p) >= 4])
    return {p for p in perms if p == p[::-1]}