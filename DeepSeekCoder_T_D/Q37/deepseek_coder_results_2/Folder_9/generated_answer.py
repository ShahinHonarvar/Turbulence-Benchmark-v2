def filter_chars(s):
    for i in range(38, 100):
        if 'A' <= s[i] <= 'Q':
            s = s.replace(s[i], '')
    return s