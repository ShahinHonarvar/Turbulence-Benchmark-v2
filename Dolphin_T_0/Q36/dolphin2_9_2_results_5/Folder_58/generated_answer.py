def filter_chars(s):
    for c in range(318, 337):
        if 'B' < s[c] < 'z':
            s = s.replace(s[c], '')
    return s