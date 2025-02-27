def filter_chars(s):
    for i in range(34, 68):
        if 'W' <= s[i] <= 'x':
            s = s[:i] + s[i + 1:]
    return s