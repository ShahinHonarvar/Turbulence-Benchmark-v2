def filter_chars(s):
    for i in range(1, 6):
        if len(s) > i and s[i] >= '$' and (s[i] <= ';'):
            s = s.replace(s[i], '')
    return s