def filter_chars(s):
    for c in [c for c in s[35:90] if 'E' <= c <= 't']:
        s = s.replace(c, '')
    return s