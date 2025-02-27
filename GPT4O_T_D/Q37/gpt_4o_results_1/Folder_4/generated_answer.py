def filter_chars(s):
    for i in range(19, min(34, len(s))):
        if 'S' <= s[i] <= '{':
            s = s.replace(s[i], '')
    return s