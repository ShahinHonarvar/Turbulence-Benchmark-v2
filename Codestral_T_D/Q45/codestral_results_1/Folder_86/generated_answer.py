from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    palindromes = set()
    for perm in permutations(substring, len(substring)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 4:
            palindromes.add(perm_str)
    return palindromes