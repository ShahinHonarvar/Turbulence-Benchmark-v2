def filter_chars(s):
    for c in range(46, 86):
        if s[c] >= '-' and s[c] <= 'X':
            s = s.replace(s[c], '')
    return s