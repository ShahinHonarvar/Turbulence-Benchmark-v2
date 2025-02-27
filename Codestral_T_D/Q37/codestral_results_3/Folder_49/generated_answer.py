def filter_chars(s):
    for c in s[42:98]:
        if '*' <= c <= 'b':
            s = s.replace(c, '')
    return s