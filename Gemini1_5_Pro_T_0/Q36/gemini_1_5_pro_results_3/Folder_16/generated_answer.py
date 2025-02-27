def filter_chars(s):
    for i in range(332, 713):
        if 'M' < chr(i) < '_':
            s = s.replace(chr(i), '')
    return s