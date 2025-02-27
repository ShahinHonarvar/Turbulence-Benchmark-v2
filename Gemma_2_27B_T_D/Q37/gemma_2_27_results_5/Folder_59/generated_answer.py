def filter_chars(s):
    for i in range(2, 4):
        if s[i] >= '5' and s[i] <= '_':
            s = s.replace(s[i], '')
    return s