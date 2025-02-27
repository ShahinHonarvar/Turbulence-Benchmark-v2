def filter_chars(s):
    for c in [c for c in s[1:8] if 'L' <= c <= 'a']:
        s = s.replace(c, '')
    return s