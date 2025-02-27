def filter_chars(s):
    for c in s[13:29]:
        if 'c' <= c <= 'n':
            s = s.replace(c, '')
    return s