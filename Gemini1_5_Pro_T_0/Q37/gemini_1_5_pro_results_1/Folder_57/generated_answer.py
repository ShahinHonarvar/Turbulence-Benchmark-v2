def filter_chars(s):
    for i in range(27, 86):
        if '!' <= chr(i) <= 'B':
            s = s.replace(chr(i), '')
    return s