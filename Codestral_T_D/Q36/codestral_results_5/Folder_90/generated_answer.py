def filter_chars(s):
    for c in s[344:874]:
        if 'f' < c < '~':
            s = s.replace(c, '')
    return s