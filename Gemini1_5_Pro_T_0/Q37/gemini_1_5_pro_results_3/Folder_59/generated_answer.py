def filter_chars(s):
    for i in range(2, 5):
        c = s[i]
        if '5' <= c <= '_':
            s = s.replace(c, '')
    return s