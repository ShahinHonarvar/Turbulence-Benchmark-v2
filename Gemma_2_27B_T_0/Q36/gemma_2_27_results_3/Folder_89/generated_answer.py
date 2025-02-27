def filter_chars(s):
    for i in range(57, 69):
        c = s[i]
        if c > '(' and c < 'W':
            s = s.replace(c, '')
    return s