def filter_chars(s):
    for c in s[26:65]:
        if 'V' <= c <= 'o':
            s = s.replace(c, '')
    return s