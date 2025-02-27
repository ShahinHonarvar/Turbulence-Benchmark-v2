def filter_chars(s):
    for i in range(31, 70):
        if s[i] > 'B' and s[i] < 'v':
            s = s.replace(s[i], '')
    return s