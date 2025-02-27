def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 344 < i < 874 and 'f' < c < '~':
            t = t.replace(c, '')
        else:
            t += c
    return t