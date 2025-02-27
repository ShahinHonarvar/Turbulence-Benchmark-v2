def filter_chars(s):
    for i in range(19, 91):
        if 'F' <= s[i] <= 'h':
            s = s.replace(s[i], '')
    return s