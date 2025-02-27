from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[4:8].lower()
    english_letters = ''.join((char for char in substring if char.isalpha()))
    if len(english_letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(english_letters) + 1):
        for perm in set(permutations(english_letters, length)):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes