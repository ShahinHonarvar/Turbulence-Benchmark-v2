def palindromes_of_specific_lengths(s):
    res = set()
    sub = s[127:289]
    for i in range(119, 142):
        for p in range(len(sub) - i):
            pal = sub[p:p + i]
            if pal == pal[::-1] and pal.lower() == pal:
                res.add(pal)
    return res