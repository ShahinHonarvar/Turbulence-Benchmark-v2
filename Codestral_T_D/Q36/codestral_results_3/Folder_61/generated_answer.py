def filter_chars(s):
    for c in s[3:9]:
        if '*' < c < 'E':
            s = s.replace(c, '')
    return s