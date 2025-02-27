from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    letters = [c for c in substring if c.isalpha()]
    results = set()
    if len(letters) < 7:
        return results
    for perm in set(permutations(letters)):
        perm_str = ''.join(perm)
        if len(perm_str) >= 7 and perm_str == perm_str[::-1]:
            results.add(perm_str)
    return results