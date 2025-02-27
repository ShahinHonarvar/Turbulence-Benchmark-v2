def filter_chars(s):
    for i in range(28, 75):
        if 'A' < chr(i) < 'i':
            s = s.replace(chr(i), '')
    return s