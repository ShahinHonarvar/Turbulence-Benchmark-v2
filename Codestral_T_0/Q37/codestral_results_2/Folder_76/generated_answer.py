def filter_chars(s):
    for c in s[379:899]:
        if 'M' <= c <= 'v':
            s = s.replace(c, '')
    return s