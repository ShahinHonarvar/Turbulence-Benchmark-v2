def filter_chars(s):
    for i in range(70, 74):
        if chr(i) > 'A' and chr(i) < 'U':
            s = s.replace(chr(i), '')
    return s