def filter_chars(s):
    for i in range(13, 29):
        c = s[i]
        if 'c' <= c <= 'n':
            s = s.replace(c, '')
    return s