from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    substring = string[0:3]
    perms = permutations(substring)
    palindromes = set()
    for perm in perms:
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes