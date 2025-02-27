def filter_chars(s):
    for c in s[19:69]:
        if '<' < c < 'C':
            s = s.replace(c, '')
    return s