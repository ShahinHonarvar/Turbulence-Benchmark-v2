def filter_chars(s):
    res = ''
    for i in range(len(s)):
        c = s[i]
        if not (29 <= i <= 79 and 'K' <= c <= 'z'):
            res += c
    return res