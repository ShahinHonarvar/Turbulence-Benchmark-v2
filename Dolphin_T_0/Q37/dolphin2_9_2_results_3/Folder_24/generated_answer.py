def filter_chars(s):
    for i in range(36, 80):
        if s[i] >= '2' and s[i] <= 's':
            s = s.replace(s[i], '')
    return s