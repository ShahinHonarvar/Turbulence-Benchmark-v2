def filter_chars(s):
    for i in range(8, 10):
        if 'R' <= s[i] <= 't':
            s = s.replace(s[i], '')
    return s