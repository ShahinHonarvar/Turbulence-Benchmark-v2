from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindromes = set()
    perms = set(permutations(s))
    for perm in perms:
        if len(perm) >= 3 and perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes