def filter_chars(s):
    for i in range(603, 760):
        if s[i] >= 'Q' and s[i] <= 'h':
            s = s[:i] + s[i + 1:]
    return s