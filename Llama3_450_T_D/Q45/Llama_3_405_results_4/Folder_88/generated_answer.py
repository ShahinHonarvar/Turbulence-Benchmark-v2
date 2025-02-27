from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:8].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(6, len(s) + 1):
        for perm in permutations(s, r):
            perm = ''.join(perm)
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes