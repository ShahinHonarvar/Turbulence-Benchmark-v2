def filter_chars(s):
    for c in s[81:86]:
        if '!' < c < 's':
            s = s.replace(c, '')
    return s