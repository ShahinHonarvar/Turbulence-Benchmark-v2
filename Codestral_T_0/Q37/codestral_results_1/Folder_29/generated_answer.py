def filter_chars(s):
    for c in sorted(set(s[12:89])):
        if '&' <= c <= 'v':
            s = s.replace(c, '')
    return s