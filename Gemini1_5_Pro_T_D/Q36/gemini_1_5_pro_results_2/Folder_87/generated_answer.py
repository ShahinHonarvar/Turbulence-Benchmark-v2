def filter_chars(s):
    for i in range(33, 61):
        if chr(i) > '3' and chr(i) < 'D':
            s = s.replace(chr(i), '')
    return s