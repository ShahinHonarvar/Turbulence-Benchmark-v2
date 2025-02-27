from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    palindromes = set()
    for perm in permutations(s):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            palindromes.add(perm_str)
    return palindromes