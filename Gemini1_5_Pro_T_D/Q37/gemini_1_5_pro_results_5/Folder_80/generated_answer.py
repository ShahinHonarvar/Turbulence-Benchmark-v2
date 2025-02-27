def filter_chars(s):
    for i in range(36, 80):
        c = s[i]
        if 'a' <= c <= 'i':
            s = s.replace(c, '')
    return s