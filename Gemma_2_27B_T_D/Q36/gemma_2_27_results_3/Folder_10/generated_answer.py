def filter_chars(s):
    for i in range(35, 60):
        c = s[i]
        if c > '!' and c < 'B':
            s = s.replace(c, '')
    return s