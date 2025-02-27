from itertools import permutations, combinations
    from collections import Counter

def palindromes_between_indices(s):
    res = set()
    letters = [a for a in s[1:7] if a.isalpha()]
    if len(set(letters)) < 2 or len(letters) < 3:
        return res
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            if p == p[::-1]:
                res.add(''.join(p))
    return res