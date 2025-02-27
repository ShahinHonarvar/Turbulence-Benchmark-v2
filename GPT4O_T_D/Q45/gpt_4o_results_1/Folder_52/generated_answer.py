from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[0:8]
    letters = [char.lower() for char in substring if char.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for p in permutations(letters, length):
            perm_str = ''.join(p)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes