def filter_chars(s):
    for c in set(s[22:86]):
        if '7' <= c <= 'e':
            s = s.replace(c, '')
    return s