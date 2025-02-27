def filter_chars(s):
    for c in s[88:91]:
        if 'J' <= c <= 'Q':
            s = s.replace(c, '')
    return s