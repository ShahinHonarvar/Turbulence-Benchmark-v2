def filter_chars(s):
    for i in range(44, 59):
        if i >= len(s):
            break
        c = s[i]
        if c > '/' and c < '6':
            s = s.replace(c, '')
    return s