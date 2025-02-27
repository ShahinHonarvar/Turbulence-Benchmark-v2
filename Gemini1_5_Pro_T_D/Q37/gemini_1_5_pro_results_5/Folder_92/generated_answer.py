def filter_chars(s):
    for i in range(4, 5):
        if s[i] >= '7' and s[i] <= 'o':
            s = s.replace(s[i], '')
    return s