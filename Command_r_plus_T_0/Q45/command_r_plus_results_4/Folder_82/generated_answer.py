from itertools import permutations

def palindromes_between_indices(s):
    letters = [char for char in s[1:7] if char.isalpha()]
    letters = [char.lower() for char in letters]
    all_permutations = permutations(letters)
    palindromes = set()
    for perm in all_permutations:
        perm_str = ''.join(perm)
        if len(perm_str) >= 7 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes