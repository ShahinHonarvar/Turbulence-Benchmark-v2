def if_contains_anagrams(s):
    n = len(s)
    w = {}
    c = 0
    l = 3
    s = [''.join(sorted([*x.lower()])) for x in s if len(x) >= l]
    for i in range(n):
        if s[i] in w:
            c += w[s[i]]
            w[s[i]] += 1
            if c >= 46:
                return True
        else:
            w[s[i]] = 1
    return False