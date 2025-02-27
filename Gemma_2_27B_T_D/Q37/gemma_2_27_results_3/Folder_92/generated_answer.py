def filter_chars(s):
    for i in range(4, 5):
        for c in s:
            if c >= '7' and c <= 'o':
                s = s.replace(c, '')
    return s