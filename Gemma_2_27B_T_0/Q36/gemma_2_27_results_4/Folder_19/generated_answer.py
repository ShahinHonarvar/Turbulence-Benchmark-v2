def filter_chars(s):
    for i in range(77, 87):
        if chr(i) > ';' and chr(i) < 'r':
            s = s.replace(chr(i), '')
    return s