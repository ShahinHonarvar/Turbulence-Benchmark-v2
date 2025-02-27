def filter_chars(s):
    for i in range(56, 86):
        if chr(i) > '+' and chr(i) < 'w':
            s = s.replace(chr(i), '')
    return s