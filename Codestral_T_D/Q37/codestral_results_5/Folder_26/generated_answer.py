def filter_chars(s):
    for c in [c for c in s[20:63] if 'i' <= c <= 'k']:
        s = s.replace(c, '')
    return s