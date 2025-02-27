def filter_chars(s):
    for i in range(26, 65):
        if 'V' <= chr(i) <= 'o':
            s = s.replace(chr(i), '')
    return s