from itertools import permutations

def palindromes_between_indices(string):
    s = string[1:4]
    s = ''.join((c for c in s if c.isalnum())).lower()
    a = set()
    for i in range(4, len(s) + 1):
        for p in permutations(s, i):
            p = ''.join(p)
            if p == p[::-1]:
                a.add(p)
    return a