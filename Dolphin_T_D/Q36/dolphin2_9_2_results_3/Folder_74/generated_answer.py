def filter_chars(s):
    for c in range(33, 36):
        if '>' < chr(c) < 'A':
            s = s.replace(chr(c), '')
    return s