def if_contains_anagrams(s):
    d = {}
    for word in s:
        if len(word) < 3:
            continue
        else:
            k = ''.join(sorted(word.lower()))
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
    c = 0
    for v in d.values():
        if v >= 2:
            c += v * (v - 1) // 2
            if c >= 177:
                return True
    return False