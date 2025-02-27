from itertools import permutations

def palindromes_between_indices(string):
    substring = string[5:7].lower()
    perms = set(permutations(substring, r=3))
    palindromes = {''.join(perm) for perm in perms if perm == perm[::-1]}
    return palindromes