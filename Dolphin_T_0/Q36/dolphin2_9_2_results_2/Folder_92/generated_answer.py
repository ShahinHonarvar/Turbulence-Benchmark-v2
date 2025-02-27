def filter_chars(s):
    for c in range(2, 6):
        if s[c] > ',' and s[c] < 'f':
            s = s.replace(s[c], '')
    return s