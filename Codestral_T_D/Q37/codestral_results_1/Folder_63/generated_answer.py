def filter_chars(s):
    for c in [c for c in s[42:93] if '/' <= c <= 'a']:
        s = s.replace(c, '')
    return s