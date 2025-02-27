def filter_chars(s):
    for c in s[45:57]:
        if 'F' < c < 'n':
            s = s.replace(c, '')
    return s