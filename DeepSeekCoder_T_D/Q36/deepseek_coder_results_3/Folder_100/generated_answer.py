def filter_chars(s):
    for i in range(44, 69):
        if 'B' < s[i] < 'r':
            s = s.replace(s[i], '')
    return s