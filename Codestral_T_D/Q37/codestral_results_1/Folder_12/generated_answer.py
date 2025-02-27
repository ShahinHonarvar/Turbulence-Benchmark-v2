def filter_chars(s):
    for c in s[19:91]:
        if 'F' <= c <= 'h':
            s = s.replace(c, '')
    return s