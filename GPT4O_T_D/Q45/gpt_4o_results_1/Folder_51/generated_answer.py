from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substring = s[3:6].lower()
    filtered = ''.join([ch for ch in substring if ch.isalpha()])
    palindromes = set()
    for i in range(3, len(filtered) + 1):
        for perm in permutations(filtered, i):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes