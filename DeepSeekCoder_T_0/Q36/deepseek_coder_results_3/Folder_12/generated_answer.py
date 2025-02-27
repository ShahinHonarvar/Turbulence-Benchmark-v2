def filter_chars(s):
    for i in range(33, 84):
        if 'm' < chr(i) < 'w':
            s = s.replace(chr(i), '')
    return s