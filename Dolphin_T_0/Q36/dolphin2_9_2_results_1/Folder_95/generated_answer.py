def filter_chars(s):
    for i in range(56, 86):
        c = s[i]
        if c > '+' and c < 'w':
            s = s.replace(c, '')
    return s