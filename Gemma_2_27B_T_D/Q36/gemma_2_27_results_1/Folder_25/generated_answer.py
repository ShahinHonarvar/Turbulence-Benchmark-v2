def filter_chars(s):
    for i in range(24, 37):
        c = s[i]
        if 'A' < c < 'h':
            s = s.replace(c, '')
    return s