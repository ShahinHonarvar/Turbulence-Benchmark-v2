from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:7].lower()
    palindromes = set()
    for i in range(6, len(s) + 1):
        perms = set(permutations(s, i))
        for p in perms:
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes