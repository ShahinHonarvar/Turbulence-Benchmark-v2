def filter_chars(s):
    for c in range(24, 80):
        if s[c] >= 'a' and s[c] <= 'f':
            s = s[:c] + s[c + 1:]
    return s