def filter_chars(s):
    for i in range(138, 921):
        if '6' <= s[i] <= 'A':
            s = s[:i] + s[i + 1:]
    return s