def filter_chars(s):
    for c in s[82:89]:
        if '*' < c < '[':
            s = s.replace(c, '')
    return s