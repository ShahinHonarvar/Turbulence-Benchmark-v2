def filter_chars(s):
    for i in range(25, 37):
        if 'A' < s[i] < 'h':
            s = s.replace(s[i], '')
    return s