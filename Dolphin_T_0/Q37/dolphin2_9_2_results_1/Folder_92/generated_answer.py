def filter_chars(s):
    for c in s:
        if '4' <= c <= 'o':
            s = s.replace(c, '')
    return s