def filter_chars(s):
    for i in range(52, 88):
        if chr(i) > '&' and chr(i) < 'c':
            s = s.replace(chr(i), '')
    return s