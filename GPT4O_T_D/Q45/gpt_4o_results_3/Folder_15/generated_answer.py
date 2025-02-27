from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:3].lower()
    if not s.isalpha() or len(s) < 3:
        return set()
    perms = set(permutations(s))
    result = set()
    for perm in perms:
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            result.add(perm_str)
    return result