from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 3:
        return set()
    substring = s[:3].lower()
    letters = ''.join(filter(str.isalpha, substring))
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes