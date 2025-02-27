def filter_chars(s):
    for i in range(21, 25):
        c = s[i]
        if c > '5' and c < '}':
            s = s.replace(c, '')
    return s