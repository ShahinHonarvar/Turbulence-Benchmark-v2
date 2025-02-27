from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substring = s[3:7].lower()
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 4 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes