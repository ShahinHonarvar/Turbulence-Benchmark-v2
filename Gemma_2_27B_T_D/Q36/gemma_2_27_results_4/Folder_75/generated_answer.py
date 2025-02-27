def filter_chars(s):
    for i in range(46, 74):
        if chr(i) > '&' and chr(i) < 'M':
            s = s.replace(chr(i), '')
    return s