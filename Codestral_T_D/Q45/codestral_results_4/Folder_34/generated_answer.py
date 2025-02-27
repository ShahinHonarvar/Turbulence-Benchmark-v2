from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:8].lower()
    palindromes = set()
    for length in range(4, len(s) + 1):
        perms = set(permutations(s, length))
        for perm in perms:
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes