from itertools import permutations

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = ''.join((c for c in s if c in english_letters))
    if len(s) < 7 or 8 - 3 + 1 < 7:
        return set()
    substr = s[3:9]
    perms = set((''.join(perm) for i in range(7, len(substr) + 1) for perm in permutations(substr, i)))
    palindromes = {perm for perm in perms if perm == perm[::-1]}
    return palindromes