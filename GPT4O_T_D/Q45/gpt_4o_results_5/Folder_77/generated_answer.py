from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substring = s[4:7].lower()
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for perm in permutations(letters, i):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes