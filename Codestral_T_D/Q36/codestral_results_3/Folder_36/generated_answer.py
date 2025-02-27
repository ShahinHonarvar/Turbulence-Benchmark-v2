def filter_chars(s):
    for c in s[283:484]:
        if 'l' < c < 't':
            s = s.replace(c, '')
    return s