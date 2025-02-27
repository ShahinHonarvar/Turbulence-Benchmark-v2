def filter_chars(s):
    for c in s[44:48]:
        if '+' < c < 'l':
            s = s.replace(c, '')
    return s