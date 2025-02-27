from itertools import permutations

def palindromes_between_indices(s):
    sub = s[4:9].lower()
    sub = ''.join(filter(str.isalpha, sub))
    if len(sub) < 6:
        return set()
    palindromes = set()
    for perm in permutations(sub):
        perm_str = ''.join(perm)
        if len(perm_str) >= 6 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes