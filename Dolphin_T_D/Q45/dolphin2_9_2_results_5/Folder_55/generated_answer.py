from collections import Counter

def palindromes_between_indices(s):
    c = Counter(s[0:3].lower())
    p = []
    for v in c.values():
        if v > 1:
            if v % 2 == 0:
                p += ['a' * v]
            if v > 2 and v % 2 == 1:
                p += ['a' * (v - 1) + 'B' + 'a' * (v - 1)]
    return set(p)