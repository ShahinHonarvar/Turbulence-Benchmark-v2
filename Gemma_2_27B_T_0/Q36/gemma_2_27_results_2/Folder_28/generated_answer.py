def filter_chars(s):
    for i in range(31, 73):
        if chr(i) > 'M' and chr(i) < 'j':
            s = s.replace(chr(i), '')
    return s