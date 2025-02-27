def filter_chars(s):
    for i, c in enumerate(s[51:97]):
        if c >= 'X' and c <= 'p':
            s = s.replace(c, '')
    return s