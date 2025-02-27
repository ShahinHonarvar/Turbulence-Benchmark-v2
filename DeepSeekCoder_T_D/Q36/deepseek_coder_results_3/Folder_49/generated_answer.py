def filter_chars(s):
    for c in range(47, 91):
        if 'D' < chr(c) < 'H':
            s = s.replace(chr(c), '')
    return s