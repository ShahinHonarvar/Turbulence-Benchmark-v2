def filter_chars(s):
    for i in range(379, 899):
        if 'M' <= s[i] <= 'v':
            s = s[:i] + s[i + 1:]
    return s