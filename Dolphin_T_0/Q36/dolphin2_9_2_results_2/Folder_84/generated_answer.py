def filter_chars(s):
    for c in range(171, 636):
        if s[c] > 'c' and s[c] < 's':
            s = s[:c] + s[c + 1:]
    return s