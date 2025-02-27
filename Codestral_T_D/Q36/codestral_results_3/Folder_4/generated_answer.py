def filter_chars(s):
    for c in s[42:67]:
        if '6' < c < 'g':
            s = s.replace(c, '')
    return s