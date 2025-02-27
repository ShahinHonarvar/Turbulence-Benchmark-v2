from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[3:8].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in set(permutations(letters)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            palindromes.add(perm_str)
    return palindromes