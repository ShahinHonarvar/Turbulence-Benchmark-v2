def filter_chars(s):
    res = []
    for i, c in enumerate(s):
        if 42 <= i < 67 and '6' < c < 'g':
            s = s.replace(c, '')
    return s