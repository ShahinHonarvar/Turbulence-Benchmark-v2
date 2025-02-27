def filter_chars(s):
    for i in range(1, 6):
        c = s[i]
        if '$' <= c <= ';':
            s = s.replace(c, '')
    return s