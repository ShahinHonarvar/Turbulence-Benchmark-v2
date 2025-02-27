def filter_chars(s):
    for c in sorted(set(s[51:97])):
        if 'X' <= c <= 'p':
            s = s.replace(c, '')
    return s