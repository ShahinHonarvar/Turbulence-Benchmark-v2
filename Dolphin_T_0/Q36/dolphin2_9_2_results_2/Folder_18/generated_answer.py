def filter_chars(s):
    for c in s[587:648]:
        if ',' < c < 'c':
            s = s.replace(c, '')
    return s