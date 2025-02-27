def filter_chars(s):
    for i in range(27, 86):
        if 'c' <= s[i] <= 'i':
            s = s.replace(s[i], '')
    return s