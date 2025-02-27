from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    pals = set()
    for i in range(5, len(s) + 1):
        for p in permutations(s, i):
            if p == p[::-1]:
                pals.add(''.join(p))
    return pals