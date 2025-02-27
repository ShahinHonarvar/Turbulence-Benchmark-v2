def filter_chars(s):
    for c in s[27:86]:
        if 'c' <= c <= 'i':
            s = s.replace(c, '')
    return s