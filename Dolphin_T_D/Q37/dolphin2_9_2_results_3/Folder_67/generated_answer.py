def filter_chars(s):
    for c in range(19, 23):
        if s[c] >= ']' and s[c] <= 't':
            s = s.replace(s[c], '')
    return s