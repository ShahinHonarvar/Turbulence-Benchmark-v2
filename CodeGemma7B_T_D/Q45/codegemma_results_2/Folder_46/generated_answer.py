from itertools import permutations

def palindromes_between_indices(s):
    index = s[4:10]
    if not index.isalpha():
        return set()
    index = [i.lower() for i in index]
    res = set()
    for p in permutations(index):
        p = ''.join(p)
        if len(p) >= 6 and p == p[::-1]:
            res.add(p)
    return res