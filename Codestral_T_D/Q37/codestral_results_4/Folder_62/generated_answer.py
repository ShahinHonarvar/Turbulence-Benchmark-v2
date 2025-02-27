def filter_chars(s):
    for c in set(s[10:70]):
        if 'I' <= c <= 'K':
            s = s.replace(c, '')
    return s