def filter_chars(s):
    for c in [c for c in s[12:89] if '&' <= c <= 'v']:
        s = s.replace(c, '')
    return s