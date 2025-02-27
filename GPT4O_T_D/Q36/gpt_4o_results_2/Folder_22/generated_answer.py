def filter_chars(s):
    if len(s) <= 55:
        return s
    for c in set(s[56:84]):
        if ';' < c < 'z':
            s = s.replace(c, '')
    return s