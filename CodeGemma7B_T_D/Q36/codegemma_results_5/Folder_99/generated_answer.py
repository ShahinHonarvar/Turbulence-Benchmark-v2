def filter_chars(s):
    for i in range(476, 948):
        if s[i] in range('b', 'd'):
            s = s.replace(s[i], '')
    return s