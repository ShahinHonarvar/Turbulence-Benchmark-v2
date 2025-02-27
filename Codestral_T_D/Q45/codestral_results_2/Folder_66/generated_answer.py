from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    subset = string[0:6]
    perms = permutations(subset)
    palindromes = set()
    for perm in perms:
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 5:
            palindromes.add(perm_str)
    return palindromes