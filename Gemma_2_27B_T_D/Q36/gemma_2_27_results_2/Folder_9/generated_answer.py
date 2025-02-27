def filter_chars(s):
    for i in range(50, 92):
        c = s[i]
        if c > 'A' and c < 'Q':
            s = s.replace(c, '')
    return s