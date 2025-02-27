from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:8].lower()
    s = ''.join(filter(str.isalpha, s))
    pals = set()
    for r in range(5, len(s) + 1):
        for p in permutations(s, r):
            if p == p[::-1]:
                pals.add(''.join(p))
    return pals