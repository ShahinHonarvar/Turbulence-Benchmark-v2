def filter_chars(s):
    for i in range(67, 90):
        if '#' < chr(i) < 'T':
            s = s.replace(chr(i), '')
    return s