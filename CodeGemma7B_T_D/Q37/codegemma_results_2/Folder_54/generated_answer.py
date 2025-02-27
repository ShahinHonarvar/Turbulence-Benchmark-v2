def filter_chars(s):
    for i in range(46, 86):
        s = s.replace(chr(i), '')
    return s