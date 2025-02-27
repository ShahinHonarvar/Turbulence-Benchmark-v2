from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:7].lower()
    perms = set(permutations(substring))
    palindromes = set()
    for perm in perms:
        if len(perm) >= 3 and perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes