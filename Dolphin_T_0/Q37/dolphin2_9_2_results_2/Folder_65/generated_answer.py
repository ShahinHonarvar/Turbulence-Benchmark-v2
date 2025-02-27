def filter_chars(s):
    for i in range(61, 71):
        c = s[i]
        if '0' <= c <= '@':
            s = s.replace(c, '')
    return s