from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substr = ''.join(filter(str.isalpha, s[6:10]))
    possible_permutations = set(permutations(substr))
    palindromes = set()
    for perm in possible_permutations:
        perm_str = ''.join(perm)
        n = len(perm_str)
        if n >= 5 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes