def filter_chars(s):
    for c in s[502:946]:
        if 'W' < c < 'y':
            s = s.replace(c, '')
    return s