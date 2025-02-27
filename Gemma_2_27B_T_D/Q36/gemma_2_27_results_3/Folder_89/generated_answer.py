def filter_chars(s):
    for i in range(57, 69):
        if chr(i) > '(' and chr(i) < 'W':
            s = s.replace(chr(i), '')
    return s