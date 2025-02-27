def filter_chars(s):
    for i in range(24, 80):
        if i < len(s):
            c = s[i]
            if 'a' <= c <= 'f':
                s = s.replace(c, '')
    return s