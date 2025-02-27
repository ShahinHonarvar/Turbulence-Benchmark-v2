def filter_chars(s):
    for i in range(331, 713):
        if i >= len(s):
            break
        c = s[i]
        if 'M' < c < '_':
            s = s.replace(c, '')
    return s