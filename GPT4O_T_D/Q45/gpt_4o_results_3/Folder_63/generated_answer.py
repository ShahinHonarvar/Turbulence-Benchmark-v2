from itertools import permutations

def palindromes_between_indices(s):
    substr = s[0:4].lower()
    substr = ''.join(filter(str.isalpha, substr))
    unique_palindromes = set()
    for perm in set(permutations(substr)):
        perm_str = ''.join(perm)
        if len(perm_str) >= 3 and perm_str == perm_str[::-1]:
            unique_palindromes.add(perm_str)
    return unique_palindromes