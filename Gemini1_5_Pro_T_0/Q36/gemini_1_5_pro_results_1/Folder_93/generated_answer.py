def filter_chars(s):
    for i in range(52, 88):
        if i < len(s) and s[i] > '&' and (s[i] < 'c'):
            s = s.replace(s[i], '')
    return s