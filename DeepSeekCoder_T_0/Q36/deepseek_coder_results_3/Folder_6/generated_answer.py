def filter_chars(s):
    for i in range(32, 69):
        if 'B' < s[i] < 'v':
            s = s.replace(s[i], '')
    return s