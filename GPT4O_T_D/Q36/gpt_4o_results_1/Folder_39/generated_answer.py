def filter_chars(s):
    for c in s[44:59]:
        if '5' < c < 'C':
            s = s.replace(c, '')
    return s