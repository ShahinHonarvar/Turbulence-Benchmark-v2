def filter_chars(s):
    for i in range(66, 90):
        if chr(i) > '#' and chr(i) < 'T':
            s = s.replace(chr(i), '')
    return s