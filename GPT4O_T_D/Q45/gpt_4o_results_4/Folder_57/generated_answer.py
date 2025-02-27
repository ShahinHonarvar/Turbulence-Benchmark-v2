from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    letters = [char for char in substring if char.isalpha()]
    result_set = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and perm_str == perm_str[::-1]:
            result_set.add(perm_str)
    return result_set