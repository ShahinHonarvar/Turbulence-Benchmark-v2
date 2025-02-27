from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    palindromes = set()
    for perm in permutations(substring):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 3:
            palindromes.add(perm_str)
    return palindromes