def filter_chars(s):
    for c in s[48:75]:
        if '6' < c < '_':
            s = s.replace(c, '')
    return s