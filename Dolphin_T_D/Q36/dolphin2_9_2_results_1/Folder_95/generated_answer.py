def filter_chars(s):
    for c in range(56, 86):
        if s[c] > '+' and s[c] < 'w':
            s = s[:c] + s[c + 1:]
    return s