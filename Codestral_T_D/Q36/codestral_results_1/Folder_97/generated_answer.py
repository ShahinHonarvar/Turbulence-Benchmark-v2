def filter_chars(s):
    for c in s[309:591]:
        if 'S' < c < 'm':
            s = s.replace(c, '')
    return s