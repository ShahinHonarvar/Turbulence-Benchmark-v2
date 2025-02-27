def filter_chars(s):
    for i in range(31, 70):
        if chr(i) > 'B' and chr(i) < 'v':
            s = s.replace(chr(i), '')
    return s