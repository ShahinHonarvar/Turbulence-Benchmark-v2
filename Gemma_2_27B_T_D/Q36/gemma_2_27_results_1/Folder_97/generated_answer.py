def filter_chars(s):
    for i in range(309, 591):
        c = s[i]
        if 'S' < c < 'm':
            s = s.replace(c, '')
    return s