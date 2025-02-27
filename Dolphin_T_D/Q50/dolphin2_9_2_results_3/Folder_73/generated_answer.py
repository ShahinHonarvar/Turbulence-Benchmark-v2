def if_contains_anagrams(l):
    a = [i for i in l if len(i) >= 3]
    d = {}
    c = 0
    for b in a:
        b = b.lower()
        b = ''.join(sorted(b))
        if b not in d:
            d[b] = b
        else:
            c += 1
    return c >= 91