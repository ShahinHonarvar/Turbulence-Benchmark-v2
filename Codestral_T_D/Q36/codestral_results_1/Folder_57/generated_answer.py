def filter_chars(s):
    for c in s[70:74]:
        if 'A' < c < 'U':
            s = s.replace(c, '')
    return s