def filter_chars(s):
    for c in s[31:73]:
        if 'M' < c < 'j':
            s = s.replace(c, '')
    return s