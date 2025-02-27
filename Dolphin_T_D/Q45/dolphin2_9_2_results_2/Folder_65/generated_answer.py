from collections import Counter
    import itertools

def palindromes_between_indices(s):
    p = set()
    for l in range(5, len(s) // 2 + 1):
        c = Counter(s[0:l])
        for i in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=l - c.main - c.vowels):
            if i not in p:
                p.add(p.lower())
    return p