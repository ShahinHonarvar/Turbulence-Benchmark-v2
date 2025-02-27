def filter_chars(s):
    for i in range(44, 48):
        if chr(i) > '+' and chr(i) < 'l':
            s = s.replace(chr(i), '')
    return s