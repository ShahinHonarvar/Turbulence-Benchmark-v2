def filter_chars(s):
    for c in s[55:80]:
        if 'S' < c < 's':
            s = s.replace(c, '')
    return s