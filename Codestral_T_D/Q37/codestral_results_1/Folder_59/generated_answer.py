def filter_chars(s):
    for c in s[2:4]:
        if '5' <= c <= '_':
            s = s.replace(c, '')
    return s