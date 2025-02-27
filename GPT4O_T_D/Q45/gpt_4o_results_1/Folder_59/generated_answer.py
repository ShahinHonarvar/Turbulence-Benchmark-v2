from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[8:10]
    letters_only = ''.join(filter(str.isalpha, substring)).lower()
    if not letters_only or len(letters_only) < 3:
        return set()
    unique_palindromes = set()
    for perm in permutations(letters_only):
        perm_str = ''.join(perm)
        if len(perm_str) >= 3 and perm_str == perm_str[::-1]:
            unique_palindromes.add(perm_str)
    return unique_palindromes