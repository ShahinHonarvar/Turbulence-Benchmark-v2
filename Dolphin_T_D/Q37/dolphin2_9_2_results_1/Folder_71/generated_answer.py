def filter_chars(s):
    for i in range(32, 47):
        if '0' <= chr(i) <= 'k':
            s = s.replace(chr(i), '')
    return s