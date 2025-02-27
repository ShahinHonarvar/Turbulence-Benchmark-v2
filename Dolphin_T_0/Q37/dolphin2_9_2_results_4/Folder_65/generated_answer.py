def filter_chars(s):
    for i in range(61, 71):
        c = s[i]
        if c >= '0' and c <= '@':
            s = s.replace(c, '')
    return s