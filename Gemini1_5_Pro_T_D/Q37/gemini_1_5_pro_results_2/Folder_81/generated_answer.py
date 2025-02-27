def filter_chars(s):
    res = ''
    for i in range(len(s)):
        c = s[i]
        if not (19 <= i <= 92 and '8' <= c <= 'm'):
            res += c
    return res