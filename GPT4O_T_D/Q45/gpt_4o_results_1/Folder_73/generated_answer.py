from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join([c for c in s[3:7] if c.isalpha()]).lower()
    palindromes = set()
    for perm in permutations(substring):
        perm_str = ''.join(perm)
        if len(perm_str) >= 3 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes