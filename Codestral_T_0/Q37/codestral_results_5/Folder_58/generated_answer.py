def filter_chars(s):
    for c in s[503:754]:
        if '9' <= c <= 'w':
            s = s.replace(c, '')
    return s