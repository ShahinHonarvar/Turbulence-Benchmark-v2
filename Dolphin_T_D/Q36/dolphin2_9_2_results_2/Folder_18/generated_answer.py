def filter_chars(s):
    for c in range(587, 648):
        if s[c] > ',' and s[c] < 'c':
            s = s[:c] + s[c + 1:]
    return s