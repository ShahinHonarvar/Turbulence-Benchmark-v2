def filter_chars(s):
    for i in range(69, 87):
        if chr(i) > '#' and chr(i) < 'L':
            s = s.replace(chr(i), '')
    return s