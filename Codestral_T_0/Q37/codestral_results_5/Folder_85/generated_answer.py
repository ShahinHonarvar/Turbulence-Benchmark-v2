def filter_chars(s):
    for c in s[28:66]:
        if 'O' <= c <= 'd':
            s = s.replace(c, '')
    return s