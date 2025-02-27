from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:8].lower()
    letters = [c for c in substring if c.isalpha()]
    palindromes_set = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 6 and perm_str == perm_str[::-1]:
            palindromes_set.add(perm_str)
    return palindromes_set