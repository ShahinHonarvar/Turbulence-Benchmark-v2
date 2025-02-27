from itertools import permutations

def palindromes_between_indices(s):
    sub_str = ''.join(filter(str.isalpha, s[3:10])).lower()
    palindromes = set()
    if len(sub_str) < 3:
        return palindromes
    for perm in set(permutations(sub_str)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 3:
            palindromes.add(perm_str)
    return palindromes