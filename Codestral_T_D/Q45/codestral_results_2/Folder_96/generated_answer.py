from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    palindromes = set()
    for i in range(6, len(s) + 1):
        perms = set(permutations(s, i))
        for p in perms:
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes