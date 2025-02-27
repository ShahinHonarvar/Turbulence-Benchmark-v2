import itertools

def palindromes_between_indices(s):
    s = s.lower()
    s = s[0:5]
    perms = set()
    for i in range(4, len(s) + 1):
        perms.update(map(''.join, itertools.permutations(s, i)))
    palindromes = {perm for perm in perms if perm == perm[::-1]}
    return palindromes