def filter_chars(s):
    for i in range(3, 5):
        c = s[i]
        if c > 'Y' and c < 's':
            s = s.replace(c, '')
    return s