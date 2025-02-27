def filter_chars(s):
    for i in range(43, 83):
        c = s[i]
        if c > ':' and c < 'Q':
            s = s.replace(c, '')
    return s