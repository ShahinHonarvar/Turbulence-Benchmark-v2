def filter_chars(s):
    for c in [c for c in s[10:53] if '@' <= c <= 'T']:
        s = s.replace(c, '')
    return s