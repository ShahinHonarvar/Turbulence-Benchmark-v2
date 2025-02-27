def filter_chars(s):
    for c in s[69:81]:
        if '@' <= c <= 'p':
            s = s.replace(c, '')
    return s