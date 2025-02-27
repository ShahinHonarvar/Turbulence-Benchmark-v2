def filter_chars(s):
    for i in range(318, 337):
        if chr(i) > 'B' and chr(i) < 'z':
            s = s.replace(chr(i), '')
    return s