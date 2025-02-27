def filter_chars(s):
    for c in s[0:3]:
        if '$' < c < '?':
            s = s.replace(c, '')
    return s