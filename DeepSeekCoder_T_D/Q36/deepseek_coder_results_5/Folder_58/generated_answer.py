def filter_chars(s):
    for i in range(319, 337):
        if 'B' < s[i] < 'z':
            s = s.replace(s[i], '')
    return s