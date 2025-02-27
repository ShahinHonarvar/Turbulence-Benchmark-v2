def filter_chars(s):
    for c in range(56, 86):
        if s[c] > '+' and s[c] < 'w':
            s = s.replace(s[c], '')
    return s