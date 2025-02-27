from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:7].lower()
    letters = [char for char in sub_str if char.isalpha()]
    perms = set(permutations(letters))
    palindromes = set()
    for perm in perms:
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 4:
            palindromes.add(perm_str)
    return palindromes