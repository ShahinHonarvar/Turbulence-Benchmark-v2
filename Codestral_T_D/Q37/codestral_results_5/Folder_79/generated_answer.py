def filter_chars(s):
    for c in sorted(set(s[10:53])):
        if '@' <= c <= 'T':
            s = s.replace(c, '')
    return s