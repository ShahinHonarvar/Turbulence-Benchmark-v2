def filter_chars(s):
    for c in range(81, 86):
        if c > '!' and c < 's':
            s = s.replace(chr(c), '')
    return s