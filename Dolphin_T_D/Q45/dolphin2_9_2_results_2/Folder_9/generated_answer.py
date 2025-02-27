from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    perms = permutations(s[0:7], 7)
    perms_set = set()
    for perm in perms:
        perms_set.add(''.join(perm))
    palindromes = set()
    for perm in perms_set:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes