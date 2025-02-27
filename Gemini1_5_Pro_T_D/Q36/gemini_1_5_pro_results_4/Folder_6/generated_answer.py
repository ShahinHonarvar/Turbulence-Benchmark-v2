def filter_chars(s):
    for i in range(32, 70):
        if 'B' < chr(i) < 'v':
            s = s.replace(chr(i), '')
    return s