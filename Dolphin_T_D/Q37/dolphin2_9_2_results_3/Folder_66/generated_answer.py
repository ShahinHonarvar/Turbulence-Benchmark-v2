def filter_chars(s):
    for i in range(27, 86):
        if 'c' <= s[i] <= 'i':
            s = s[:i] + s[i + 1:]
    return s