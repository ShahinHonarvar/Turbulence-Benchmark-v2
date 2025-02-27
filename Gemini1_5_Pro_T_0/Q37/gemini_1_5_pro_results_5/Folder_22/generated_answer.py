def filter_chars(s):
    for i in range(33, 71):
        if '7' <= chr(i) <= 'k':
            s = s.replace(chr(i), '')
    return s