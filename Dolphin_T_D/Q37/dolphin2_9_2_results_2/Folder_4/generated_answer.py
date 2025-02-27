def filter_chars(s):
    for i in range(19, 34):
        if 'S' <= s[i] <= '{':
            s = s[:i] + s[i + 1:]
    return s