def filter_chars(s):
    for i in range(19, 91):
        c = s[i]
        if 'F' <= c <= 'h':
            s = s.replace(c, '')
    return s