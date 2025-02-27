def filter_chars(s):
    for i in range(48, 75):
        if chr(i) > '6' and chr(i) < '_':
            s = s.replace(chr(i), '')
    return s