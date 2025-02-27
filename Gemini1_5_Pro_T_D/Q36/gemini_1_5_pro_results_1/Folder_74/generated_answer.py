def filter_chars(s):
    for i in range(34, 36):
        c = s[i]
        if c > '>' and c < 'A':
            s = s.replace(c, '')
    return s