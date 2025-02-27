def filter_chars(s):
    for i in range(227, 235):
        if s[i] >= 'D' and s[i] <= 'u':
            s = s.replace(s[i], '')
    return s