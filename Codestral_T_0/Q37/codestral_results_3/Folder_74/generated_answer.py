def filter_chars(s):
    for c in sorted(set(s[19:33])):
        if 'f' <= c <= 'o':
            s = s.replace(c, '')
    return s