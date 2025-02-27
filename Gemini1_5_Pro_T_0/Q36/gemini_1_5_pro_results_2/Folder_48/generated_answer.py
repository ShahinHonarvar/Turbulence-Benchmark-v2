def filter_chars(s):
    for i in range(154, 222):
        if i >= len(s):
            break
        c = s[i]
        if 'A' < c < 'f':
            s = s.replace(c, '')
    return s