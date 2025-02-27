def filter_chars(s):
    for i in range(71, 74):
        if 'A' < s[i] < 'U':
            s = s.replace(s[i], '')
    return s