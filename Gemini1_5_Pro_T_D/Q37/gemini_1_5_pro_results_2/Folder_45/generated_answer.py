def filter_chars(s):
    for i in range(72, 95):
        if '.' <= chr(i) <= 'b':
            s = s.replace(chr(i), '')
    return s