from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substring = s[2:5].lower()
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 2:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 4 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes