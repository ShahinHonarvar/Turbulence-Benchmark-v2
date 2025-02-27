def filter_chars(s):
    for c in range(42, 93):
        if s[c] >= '/' and s[c] <= 'a':
            s = s[:c] + s[c + 1:]
    return s