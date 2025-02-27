def filter_chars(s):
    for c in s[41:56]:
        if 'Z' < c < 'c':
            s = s.replace(c, '')
    return s