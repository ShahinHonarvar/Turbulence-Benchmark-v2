def filter_chars(s):
    for c in [c for c in s[22:86] if '7' <= c <= 'e']:
        s = s.replace(c, '')
    return s