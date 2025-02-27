def filter_chars(s):
    for i in range(19, 34):
        if len(s) > i and s[i] >= 'S' and (s[i] <= '{'):
            s = s.replace(s[i], '')
    return s