def filter_chars(s):
    for c in s[331:713]:
        if 'M' < c < '_':
            s = s.replace(c, '')
    return s