def filter_chars(s):
    for c in s[13:40]:
        if ':' < c < 'C':
            s = s.replace(c, '')
    return s