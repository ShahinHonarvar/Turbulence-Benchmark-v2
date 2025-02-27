def filter_chars(s):
    for c in s[373:902]:
        if 'T' <= c <= 'h':
            s = s.replace(c, '')
    return s