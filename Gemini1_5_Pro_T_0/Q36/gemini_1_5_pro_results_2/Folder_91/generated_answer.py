def filter_chars(s):
    for i in range(1, 3):
        if '$' < s[i] < '?':
            c = s[i]
            s = s.replace(c, '')
    return s