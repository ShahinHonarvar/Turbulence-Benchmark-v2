from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:9]
    perms = set(permutations(substring, r=None))
    perms = [''.join(perm).lower() for perm in perms]
    palindromes = {perm for perm in perms if len(perm) >= 4 and perm == perm[::-1]}
    return palindromes