def filter_chars(s):
    for i in range(318, 337):
        if 'B' < s[i] < 'z':
            s = s.replace(s[i], '')
    return s