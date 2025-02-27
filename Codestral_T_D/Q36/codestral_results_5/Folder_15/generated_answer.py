def filter_chars(s):
    for c in s[2:7]:
        if 'h' < c < 'k':
            s = s.replace(c, '')
    return s