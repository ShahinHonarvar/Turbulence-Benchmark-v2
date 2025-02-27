def filter_chars(s):
    for i in range(19, 34):
        if i < len(s) and 'S' <= s[i] <= '{':
            s = s.replace(s[i], '')
    return s