def filter_chars(s):
    for i in range(36, 80):
        for c in s:
            if c >= '2' and c <= 's' and (s.index(c) in range(36, 80)):
                s = s.replace(c, '')
    return s