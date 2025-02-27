def filter_chars(s):
    for i in range(13, 29):
        if s[i] >= 'c' and s[i] <= 'n':
            s = s.replace(s[i], '')
    return s