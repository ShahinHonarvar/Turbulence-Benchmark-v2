def filter_chars(s):
    for c in s[37:57]:
        if c >= '6' and c <= '_':
            s = s.replace(c, '')
    return s