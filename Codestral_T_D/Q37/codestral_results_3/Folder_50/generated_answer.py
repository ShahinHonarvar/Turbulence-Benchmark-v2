def filter_chars(s):
    for c in sorted(s[71:97]):
        if '_' <= c <= 'o':
            s = s.replace(c, '')
    return s