def filter_chars(s):
    for i in range(32, 73):
        if 'M' < chr(i) < 'j':
            s = s.replace(chr(i), '')
    return s