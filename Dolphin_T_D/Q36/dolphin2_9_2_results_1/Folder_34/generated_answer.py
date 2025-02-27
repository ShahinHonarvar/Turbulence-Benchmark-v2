def filter_chars(s):
    for c in s[10:79]:
        if '?' < c < 'm':
            s = s.replace(c, '')
    return s