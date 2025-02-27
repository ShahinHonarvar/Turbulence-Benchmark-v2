def filter_chars(s):
    for i in range(227, 236):
        c = s[i]
        if 'D' <= c <= 'u':
            s = s.replace(c, '')
    return s