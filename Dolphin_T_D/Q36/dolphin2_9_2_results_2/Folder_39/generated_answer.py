def filter_chars(s):
    for c in range(43, 59):
        if s[c] > '5' and s[c] < 'C':
            s = s.replace(s[c], '')
    return s