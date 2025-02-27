from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[4:9]
    letters = [char.lower() for char in substring if char.isalpha()]
    result = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and perm_str == perm_str[::-1]:
            result.add(perm_str)
    return result