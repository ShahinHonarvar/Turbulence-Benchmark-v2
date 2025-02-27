def filter_chars(s):
    for i in range(41, 65):
        if 'K' <= chr(i) <= ']':
            s = s.replace(chr(i), '')
    return s