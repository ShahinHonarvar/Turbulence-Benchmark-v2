def filter_chars(s):
    for i in range(14, 75):
        c = s[i]
        if c > '9' and c < 'K':
            s = s.replace(c, '')
    return s