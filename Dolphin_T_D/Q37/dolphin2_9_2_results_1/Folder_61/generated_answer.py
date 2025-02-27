def filter_chars(s):
    for i in range(5, 7):
        if 'G' <= s[i] <= 'p':
            s = s.replace(s[i], '')
    return s