def filter_chars(s):
    for c in set(s[124:855]):
        if '9' <= c <= 's':
            s = s.replace(c, '')
    return s