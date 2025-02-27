def filter_chars(s):
    for i in range(309, 591):
        c = s[i]
        if c > 'S' and c < 'm':
            s = s.replace(c, '')
    return s