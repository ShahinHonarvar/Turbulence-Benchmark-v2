def filter_chars(s):
    for i in range(42, 67):
        if chr(i) > '6' and chr(i) < 'g':
            s = s.replace(chr(i), '')
    return s