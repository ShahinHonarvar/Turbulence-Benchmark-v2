def filter_chars(s):
    for i in range(19, 33):
        if i < len(s):
            c = s[i]
            if 'f' <= c <= 'o':
                s = s.replace(c, '')
    return s