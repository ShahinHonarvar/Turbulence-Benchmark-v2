from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    letters = ''.join(filter(str.isalpha, substring))
    perms = set(permutations(letters))
    palindromes = set()
    for perm in perms:
        perm_str = ''.join(perm)
        length = len(perm_str)
        if length >= 4 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes