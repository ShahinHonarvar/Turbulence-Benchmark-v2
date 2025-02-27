def filter_chars(s):
    for i in range(318, 337):
        c = s[i]
        if c > 'B' and c < 'z':
            s = s.replace(c, '')
    return s