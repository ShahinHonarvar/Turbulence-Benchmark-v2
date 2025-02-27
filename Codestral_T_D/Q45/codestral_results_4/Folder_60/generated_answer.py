from itertools import permutations

def palindromes_between_indices(s):
    chars = s[3:7].lower()
    perms = set(permutations(chars, r=None))
    palindromes = {''.join(perm) for perm in perms if ''.join(perm) == ''.join(perm)[::-1] and len(perm) >= 4}
    return palindromes