def filter_chars(s):
    for c in range(69, 81):
        if '@' <= s[c] <= 'p':
            s = s[:c] + s[c + 1:]
    return s