from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:6].lower()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for perm in permutations(s, r):
            if len(perm) >= 3 and perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes