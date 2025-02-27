from itertools import permutations

def palindromes_between_indices(s):
    slice_str = ''.join(filter(str.isalpha, s[0:7]))
    slice_str = slice_str.lower()
    result = set()
    for perm in permutations(slice_str):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            result.add(perm_str)
    return result