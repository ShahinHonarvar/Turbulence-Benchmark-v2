def filter_chars(s):
    for i in range(73, 75):
        if 'U' <= s[i] <= 'l':
            s = s.replace(s[i], '')
    return s