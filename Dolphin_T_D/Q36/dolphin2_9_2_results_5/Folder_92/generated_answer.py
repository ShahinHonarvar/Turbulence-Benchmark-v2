def filter_chars(s):
    for c in s[1:6]:
        if ',' < c < 'f':
            s = s.replace(c, '')
    return s