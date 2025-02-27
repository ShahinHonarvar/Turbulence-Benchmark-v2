from itertools import permutations

def palindromes_between_indices(string):
    substring = string[3:8]
    substring = substring.lower()
    perms = set(permutations(substring))
    palindromes = set()
    for perm in perms:
        perm_str = ''.join(perm)
        if len(perm_str) >= 6 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes