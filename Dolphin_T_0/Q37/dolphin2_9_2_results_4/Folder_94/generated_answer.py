def filter_chars(s):
    for c in range(51, 97):
        if s[c] >= 'X' and s[c] <= 'p':
            s = s.replace(s[c], '')
    return s