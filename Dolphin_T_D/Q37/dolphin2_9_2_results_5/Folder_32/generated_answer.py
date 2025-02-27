def filter_chars(s):
    for i in range(23, 90):
        if 'w' <= s[i] <= '{':
            s = s[:i] + s[i + 1:]
    return s