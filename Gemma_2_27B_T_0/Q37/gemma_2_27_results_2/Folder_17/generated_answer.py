def filter_chars(s):
    for i in range(27, 30):
        if i < len(s):
            c = s[i]
            if ';' <= c <= 'b':
                s = s.replace(c, '')
    return s