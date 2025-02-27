def filter_chars(s):
    for i in range(28, 66):
        if 'O' <= s[i] <= 'd':
            s = s[:i] + s[i + 1:]
    return s