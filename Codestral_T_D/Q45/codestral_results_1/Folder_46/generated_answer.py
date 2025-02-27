from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    perms = permutations(substring)
    palindromes = set()
    for perm in perms:
        if len(perm) >= 6 and perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes