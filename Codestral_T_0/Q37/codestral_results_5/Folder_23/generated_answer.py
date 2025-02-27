def filter_chars(s):
    for c in sorted(set(s[51:78])):
        if 'V' <= c <= 'Y':
            s = s.replace(c, '')
    return s