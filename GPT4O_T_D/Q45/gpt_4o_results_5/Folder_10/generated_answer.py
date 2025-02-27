from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substring = s[:6].lower()
    english_letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for i in range(3, len(english_letters) + 1):
        perms = set(permutations(english_letters, i))
        for perm in perms:
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes