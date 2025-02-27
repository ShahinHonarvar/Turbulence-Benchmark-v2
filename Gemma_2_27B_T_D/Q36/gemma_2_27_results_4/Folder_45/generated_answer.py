def filter_chars(s):
    for i in range(81, 86):
        c = s[i]
        if c > '!' and c < 's':
            s = s.replace(c, '')
    return s