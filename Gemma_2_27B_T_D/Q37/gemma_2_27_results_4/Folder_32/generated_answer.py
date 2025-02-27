def filter_chars(s):
    for i in range(23, 90):
        if len(s) > i and 'w' <= s[i] <= '{':
            s = s.replace(s[i], '')
    return s