def filter_chars(s):
    for c in [c for c in s[41:65] if 'K' <= c <= ']']:
        s = s.replace(c, '')
    return s