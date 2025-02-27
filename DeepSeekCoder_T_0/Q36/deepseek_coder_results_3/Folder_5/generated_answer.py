def filter_chars(s):
    for i in range(56, 66):
        if 'f' < s[i] < '|':
            s = s.replace(s[i], '')
    return s