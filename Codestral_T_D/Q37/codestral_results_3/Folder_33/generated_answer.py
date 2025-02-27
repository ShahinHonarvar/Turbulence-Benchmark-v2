def filter_chars(s):
    for c in sorted(set(s[722:832])):
        if 'K' <= c <= 'm':
            s = s.replace(c, '')
    return s