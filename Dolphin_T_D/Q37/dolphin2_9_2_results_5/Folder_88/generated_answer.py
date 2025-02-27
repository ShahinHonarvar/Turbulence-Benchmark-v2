def filter_chars(s):
    for i in range(69, 81):
        if '@' <= s[i] <= 'p':
            s = s[:i] + s[i + 1:]
    return s