def filter_chars(s):
    for c in set(s[770:971]):
        if '-' <= c <= 'D':
            s = s.replace(c, '')
    return s