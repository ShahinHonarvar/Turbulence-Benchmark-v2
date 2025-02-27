import itertools

def palindromes_between_indices(s):
    s = ''.join([c.lower() for c in s[3:10] if c.isalpha()])
    res = set()
    for i in range(5, len(s) // 2 + 1):
        for p in itertools.permutations(s, i):
            p1, p2 = (''.join(p), ''.join(p)[::-1])
            if p1 != p2 and p2 in s:
                res.add(p1 + p2[::-1] + p1)
    return res