from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9]
    letters = [ch for ch in substring if ch.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm).lower()
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes