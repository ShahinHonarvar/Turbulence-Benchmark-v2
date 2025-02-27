from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join((c for c in s[1:7] if c.isalpha())).lower()
    palindromes = set()
    for length in range(6, len(substring) + 1):
        for perm in set(permutations(substring, length)):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes