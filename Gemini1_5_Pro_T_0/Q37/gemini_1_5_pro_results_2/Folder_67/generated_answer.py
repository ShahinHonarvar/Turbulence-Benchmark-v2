def filter_chars(s):
    res = ''
    for i in range(len(s)):
        c = s[i]
        if 19 <= i <= 22 and ']' <= c <= 't':
            if c not in res:
                res += c
        else:
            res += c
    return res