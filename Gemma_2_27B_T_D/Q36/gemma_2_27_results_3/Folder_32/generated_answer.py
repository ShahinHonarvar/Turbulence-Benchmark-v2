def filter_chars(s):
    for i in range(40, 63):
        if chr(i) > '7' and chr(i) < 'H':
            s = s.replace(chr(i), '')
    return s