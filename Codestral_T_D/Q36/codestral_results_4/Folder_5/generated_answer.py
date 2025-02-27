def filter_chars(s):
    for c in s[55:66]:
        if 'f' < c < '|':
            s = s.replace(c, '')
    return s