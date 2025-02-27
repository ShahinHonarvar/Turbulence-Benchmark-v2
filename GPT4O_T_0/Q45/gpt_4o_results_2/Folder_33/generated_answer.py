from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[7:10].lower()
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 4:
            palindromes.add(perm_str)
    return palindromes