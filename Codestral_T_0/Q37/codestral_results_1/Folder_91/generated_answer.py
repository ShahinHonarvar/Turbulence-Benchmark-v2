def filter_chars(s):
    for c in s[7:9]:
        if 'B' <= c <= 'H':
            s = s.replace(c, '')
    return s