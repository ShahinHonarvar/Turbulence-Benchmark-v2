from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[6:10].lower()
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes