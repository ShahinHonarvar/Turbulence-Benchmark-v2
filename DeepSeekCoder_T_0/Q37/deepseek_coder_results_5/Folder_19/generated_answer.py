def filter_chars(s):
    for i in range(35, 90):
        if 'E' <= s[i] <= 't':
            s = s.replace(s[i], '')
    return s