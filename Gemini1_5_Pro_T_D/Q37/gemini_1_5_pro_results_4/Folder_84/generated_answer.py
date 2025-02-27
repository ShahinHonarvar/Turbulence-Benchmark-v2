def filter_chars(s):
    res = ''
    for i in range(len(s)):
        c = s[i]
        if not (138 <= i <= 920 and '6' <= c <= 'A'):
            res += c
    return res