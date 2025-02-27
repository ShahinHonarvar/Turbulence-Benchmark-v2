def filter_chars(s):
    for i in range(318, 337):
        c = s[i]
        if 'B' < c < 'z':
            s = s.replace(c, '')
    return s