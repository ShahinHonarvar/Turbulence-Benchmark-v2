def filter_chars(s):
    for char in range(46, 91):
        if 'D' < chr(char) < 'H':
            s = s.replace(chr(char), '')
    return s