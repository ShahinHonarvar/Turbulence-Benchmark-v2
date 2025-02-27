def filter_chars(s):
    for i in range(221, 419):
        if chr(i) > '-' and chr(i) < 'v':
            s = s.replace(chr(i), '')
    return s