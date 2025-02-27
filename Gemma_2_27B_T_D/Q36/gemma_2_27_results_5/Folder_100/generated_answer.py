def filter_chars(s):
    for i in range(43, 69):
        if s[i] > 'B' and s[i] < 'r':
            s = s.replace(s[i], '')
    return s