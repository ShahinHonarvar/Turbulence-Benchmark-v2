def filter_chars(s):
    for c in s[56:86]:
        if '+' < c < 'w':
            s = s.replace(c, '')
    return s