def filter_chars(s):
    for i in range(10, 15):
        for c in s:
            if c > 't' and c < 'v':
                s = s.replace(c, '')
    return s