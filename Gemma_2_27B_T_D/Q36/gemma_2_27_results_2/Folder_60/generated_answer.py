def filter_chars(s):
    for i in range(23, 83):
        if len(s) > i and 'f' < s[i] < 'o':
            s = s.replace(s[i], '')
    return s