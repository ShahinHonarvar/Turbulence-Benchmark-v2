def filter_chars(s):
    for i in range(28, 66):
        c = s[i]
        if 'O' <= c <= 'd':
            s = s.replace(c, '')
    return s