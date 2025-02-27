from itertools import permutations

def palindromes_between_indices(s):
    str_between_indices = s[1:7]
    perms = permutations(str_between_indices.lower())
    palindromes = {''.join(p) for p in perms if p == p[::-1]}
    return palindromes