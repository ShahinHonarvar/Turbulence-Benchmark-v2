def filter_chars(s):
    for i in range(42, 67):
        if i < '6' and i > 'g':
            s = s.replace(i, '')
    return s