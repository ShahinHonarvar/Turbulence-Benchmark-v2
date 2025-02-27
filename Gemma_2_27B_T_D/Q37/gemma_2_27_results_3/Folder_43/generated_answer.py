def filter_chars(s):
    for i in range(15, 56):
        if i < len(s) and s[i] >= 'W' and (s[i] <= '{'):
            s = s.replace(s[i], '')
    return s