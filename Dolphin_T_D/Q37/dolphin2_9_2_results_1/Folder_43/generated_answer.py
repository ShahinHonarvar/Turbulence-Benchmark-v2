def filter_chars(s):
    for i in range(15, 56):
        if 'W' <= s[i] <= '{':
            s = s[:i] + s[i + 1:]
    return s