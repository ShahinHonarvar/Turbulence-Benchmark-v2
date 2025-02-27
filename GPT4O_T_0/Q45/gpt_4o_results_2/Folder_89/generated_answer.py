from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[5:10].lower()
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            palindromes.add(perm_str)
    return palindromes