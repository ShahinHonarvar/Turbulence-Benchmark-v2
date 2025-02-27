from itertools import permutations

def palindromes_between_indices(string):
    string = string[0:7].lower()
    perms = set(permutations(string))
    palindromes = set([''.join(p) for p in perms if ''.join(p) == ''.join(p)[::-1] and len(p) >= 7])
    return palindromes