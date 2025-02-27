def filter_chars(s):
    for c in s[43:83]:
        if ':' < c < 'Q':
            s = s.replace(c, '')
    return s