def filter_chars(s):
    for i in range(82, 86):
        c = s[i]
        if '!' < c < 's':
            s = s.replace(c, '')
    return s