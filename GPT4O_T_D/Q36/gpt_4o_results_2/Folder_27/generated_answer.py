def filter_chars(s):
    for c in set(s[49:75]):
        if '6' < c < '_':
            s = s.replace(c, '')
    return s