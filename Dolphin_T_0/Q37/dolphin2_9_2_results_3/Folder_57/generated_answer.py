def filter_chars(s):
    for i in range(27, 86):
        if '!' <= s[i] <= 'B':
            s = s[:i] + s[i + 1:]
    return s