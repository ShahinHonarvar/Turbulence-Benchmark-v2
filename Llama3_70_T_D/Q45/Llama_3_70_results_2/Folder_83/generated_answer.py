from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    s = ''.join(filter(str.isalpha, s))
    pals = set()
    for r in range(7, len(s) + 1):
        for perm in permutations(s, r):
            perm = ''.join(perm)
            if perm == perm[::-1]:
                pals.add(perm)
    return pals