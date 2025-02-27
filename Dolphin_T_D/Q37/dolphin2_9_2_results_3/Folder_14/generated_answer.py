def filter_chars(s):
    for i in range(35, 99):
        if 'A' <= s[i] <= 'b':
            s = s[:i] + s[i + 1:]
    return s