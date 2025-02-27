from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substring = s[2:5].lower()
    letters = [c for c in substring if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return {p for p in palindromes if len(p) >= 3}