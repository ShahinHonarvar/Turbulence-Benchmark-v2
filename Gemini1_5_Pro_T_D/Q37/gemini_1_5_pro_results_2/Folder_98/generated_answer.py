def filter_chars(s):
    for i in range(8, 10):
        if i < len(s) and s[i] >= 'R' and (s[i] <= 't'):
            s = s.replace(s[i], '')
    return s