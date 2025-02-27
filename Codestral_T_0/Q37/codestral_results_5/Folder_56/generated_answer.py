def filter_chars(s):
    for c in s[71:95]:
        if 'K' <= c <= 'a':
            s = s.replace(c, '')
    return s