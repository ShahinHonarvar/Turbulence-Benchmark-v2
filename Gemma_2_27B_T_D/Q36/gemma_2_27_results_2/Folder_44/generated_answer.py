def filter_chars(s):
    for i in range(18, 64):
        c = s[i]
        if c > '3' and c < 'B':
            s = s.replace(c, '')
    return s