def filter_chars(s):
    for i in range(10, 15):
        if len(s) > i and 't' < s[i] < 'v':
            s = s.replace(s[i], '')
    return s