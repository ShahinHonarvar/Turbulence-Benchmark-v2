from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    substring = string[3:10]
    perms = set(permutations(substring))
    palindromes = {''.join(perm) for perm in perms if len(perm) >= 5 and perm == perm[::-1]}
    return palindromes