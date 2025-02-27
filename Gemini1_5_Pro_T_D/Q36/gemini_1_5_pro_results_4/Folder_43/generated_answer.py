def filter_chars(s):
    for i in range(27, 75):
        if i < len(s):
            c = s[i]
            if 'A' < c < 'i':
                s = s.replace(c, '')
    return s