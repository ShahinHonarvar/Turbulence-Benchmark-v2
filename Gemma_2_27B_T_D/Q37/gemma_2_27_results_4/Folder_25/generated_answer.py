def filter_chars(s):
    for i in range(31, 39):
        if i < len(s):
            c = s[i]
            if ';' <= c <= 'g':
                s = s.replace(c, '')
    return s