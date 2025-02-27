def filter_chars(s):
    for c in s[1:7]:
        if '-' < c < 'L':
            s = s.replace(c, '')
    return s