def filter_chars(s):
    for i in range(58, 81):
        if chr(i) > '5' and chr(i) < '>':
            s = s.replace(chr(i), '')
    return s