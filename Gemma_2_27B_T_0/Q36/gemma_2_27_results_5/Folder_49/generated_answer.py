def filter_chars(s):
    for i in range(46, 91):
        if chr(i) > 'D' and chr(i) < 'H':
            s = s.replace(chr(i), '')
    return s