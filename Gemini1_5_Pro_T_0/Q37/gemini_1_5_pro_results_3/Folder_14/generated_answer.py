def filter_chars(s):
    for i in range(35, 99):
        if i <= len(s) - 1:
            c = s[i]
            if 'A' <= c <= 'b':
                s = s.replace(c, '')
    return s