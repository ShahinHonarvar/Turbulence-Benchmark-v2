def remove_repeat_chars(s):
    d = {}
    res = []
    for i in range(46, 91):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            res.append(s[i])
    for i in range(46, 91):
        if s[i] in res:
            s = s[:i] + s[i + 1:]
    return s