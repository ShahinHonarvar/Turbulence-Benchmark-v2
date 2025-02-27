from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    letters_only = [c for c in substring if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters_only, len(letters_only)):
        perm_str = ''.join(perm)
        if len(perm_str) >= 6 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes