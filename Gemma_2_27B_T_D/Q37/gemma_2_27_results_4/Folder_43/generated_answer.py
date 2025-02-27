def filter_chars(s):
    for i in range(15, 56):
        if len(s) > i and s[i] >= 'W' and (s[i] <= '{'):
            s = s.replace(s[i], '')
    return s