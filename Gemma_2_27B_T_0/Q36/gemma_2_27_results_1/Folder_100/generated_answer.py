def filter_chars(s):
    for i in range(43, 69):
        c = s[i]
        if 'B' < c < 'r':
            s = s.replace(c, '')
    return s