def filter_chars(s):
    for i in range(42, 78):
        c = s[i]
        if c > '!' and c < '?':
            s = s.replace(c, '')
    return s