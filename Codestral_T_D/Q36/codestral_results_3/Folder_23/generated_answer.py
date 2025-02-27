def filter_chars(s):
    for c in s[21:25]:
        if '5' < c < '}':
            s = s.replace(c, '')
    return s