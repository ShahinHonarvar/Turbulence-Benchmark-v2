def filter_chars(s):
    for c in s[669:888]:
        if 'B' < c < 'Y':
            s = s.replace(c, '')
    return s