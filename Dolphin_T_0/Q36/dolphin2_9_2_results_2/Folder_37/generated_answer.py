def filter_chars(s):
    for c in range(44, 59):
        if s[c] > '/' and s[c] < '6':
            s = s.replace(s[c], '')
    return s