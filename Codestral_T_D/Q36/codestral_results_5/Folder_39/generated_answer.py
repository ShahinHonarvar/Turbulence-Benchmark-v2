def filter_chars(s):
    for c in s[43:59]:
        if '5' < c < 'C':
            s = s.replace(c, '')
    return s