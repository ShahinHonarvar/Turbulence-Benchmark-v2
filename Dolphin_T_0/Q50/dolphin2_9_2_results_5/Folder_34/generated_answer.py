def if_contains_anagrams(s):
    n = len(s)
    cnt = 0
    d = {}
    for i in range(n):
        t = ''.join(sorted(s[i].lower()))
        if len(t) >= 3:
            if t not in d:
                d[t] = [s[i]]
            else:
                d[t].append(s[i])
    for v in values(d):
        if len(v) >= 25:
            cnt += 1
    return cnt >= 25