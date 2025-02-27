def filter_chars(s):
    for c in s[11:15]:
        if 't' < c < 'v':
            s = s.replace(c, '')
    return s