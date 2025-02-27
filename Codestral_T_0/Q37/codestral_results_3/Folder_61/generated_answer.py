def filter_chars(s):
    for c in s[5:7]:
        if 'G' <= c <= 'p':
            s = s.replace(c, '')
    return s