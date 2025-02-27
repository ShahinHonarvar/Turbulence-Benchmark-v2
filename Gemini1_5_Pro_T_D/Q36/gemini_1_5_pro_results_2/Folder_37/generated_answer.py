def filter_chars(s):
    for i in range(44, 59):
        if i >= len(s):
            break
        if s[i] > '/' and s[i] < '6':
            s = s.replace(s[i], '')
    return s