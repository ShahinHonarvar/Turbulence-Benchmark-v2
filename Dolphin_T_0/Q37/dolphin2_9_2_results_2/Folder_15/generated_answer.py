def filter_chars(s):
    for i in range(2, 7):
        for c in s[2:7]:
            if c >= '?' and c <= 'f':
                s = s.replace(c, '')
    return s