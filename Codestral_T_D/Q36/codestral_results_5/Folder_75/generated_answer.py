def filter_chars(s):
    for c in s[46:74]:
        if '&' < c < 'M':
            s = s.replace(c, '')
    return s