def filter_chars(s):
    for i in range(603, 760):
        c = s[i]
        if 'Q' <= c <= 'h':
            s = s.replace(c, '')
    return s