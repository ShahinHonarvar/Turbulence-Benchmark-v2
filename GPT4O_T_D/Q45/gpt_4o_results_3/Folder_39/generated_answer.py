from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6]
    s = ''.join(filter(str.isalpha, s)).lower()
    results = set()
    if len(s) < 3:
        return results
    for i in range(3, len(s) + 1):
        for perm in set(permutations(s, i)):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                results.add(perm_str)
    return results