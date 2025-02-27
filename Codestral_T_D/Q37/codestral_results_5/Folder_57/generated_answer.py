def filter_chars(s):
    for c in set(s[27:86]):
        if '!' <= c <= 'B':
            s = s.replace(c, '')
    return s