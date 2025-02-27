from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7].lower()
    perms = set(permutations(substring))
    palindromes = {''.join(perm) for perm in perms if ''.join(perm) == ''.join(perm[::-1]) and len(perm) >= 3}
    return palindromes