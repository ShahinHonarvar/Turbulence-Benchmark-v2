def filter_chars(s):
    for i in range(43, 69):
        if 'B' < s[i] < 'r':
            s = s.replace(s[i], '')
    return s