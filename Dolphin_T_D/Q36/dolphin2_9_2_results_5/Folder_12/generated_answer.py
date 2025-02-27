def filter_chars(s):
    for c in range(32, 84):
        if 'm' < chr(c) < 'w':
            s = s.replace(chr(c), '')
    return s