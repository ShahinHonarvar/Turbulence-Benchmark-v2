def filter_chars(s):
    for i in range(15, 56):
        if 'W' <= s[i] <= '{':
            s = s.replace(s[i], '')
    return s