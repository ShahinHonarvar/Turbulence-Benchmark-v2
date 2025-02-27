def filter_chars(s):
    for i in range(5, 7):
        if s[i] >= 'G' and s[i] <= 'p':
            s = s.replace(s[i], '')
    return s