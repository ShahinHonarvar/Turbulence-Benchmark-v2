def filter_chars(s):
    for c in sorted(set(s[29:80])):
        if 'K' <= c <= 'z':
            s = s.replace(c, '')
    return s