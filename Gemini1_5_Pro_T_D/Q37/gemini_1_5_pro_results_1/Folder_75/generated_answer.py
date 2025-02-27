def filter_chars(s):
    for i in range(34, 68):
        if 'W' <= chr(i) <= 'x':
            s = s.replace(chr(i), '')
    return s