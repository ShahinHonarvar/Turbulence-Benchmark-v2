def filter_chars(s):
    for i in range(2, 4):
        for c in s:
            if c >= '5' and c <= '_':
                s = s.replace(c, '')
    return s