def filter_chars(s):
    for c in range(31, 50):
        if s[c] > '/' and s[c] < 'J':
            s = s.replace(s[c], '')
    return s