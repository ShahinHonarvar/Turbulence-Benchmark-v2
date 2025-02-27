def filter_chars(s):
    for c in s[1:-1]:
        if '*' <= c <= 's':
            s = s.replace(c, '')
    return s