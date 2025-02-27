def filter_chars(s):
    for i in range(13, 29):
        if 'c' <= s[i] <= 'n':
            s = s.replace(s[i], '')
    return s