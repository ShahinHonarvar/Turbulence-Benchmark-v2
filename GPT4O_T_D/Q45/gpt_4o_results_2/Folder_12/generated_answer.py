from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    substring = s[3:9].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 4 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes