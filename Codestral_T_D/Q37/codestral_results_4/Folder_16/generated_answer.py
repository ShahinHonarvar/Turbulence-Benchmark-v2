def filter_chars(s):
    for c in s[225:382]:
        if 'D' <= c <= 'Y':
            s = s.replace(c, '')
    return s