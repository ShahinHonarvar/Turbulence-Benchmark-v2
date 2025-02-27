def filter_chars(s):
    for i in range(31, 50):
        if chr(i) > '/' and chr(i) < 'J':
            s = s.replace(chr(i), '')
    return s