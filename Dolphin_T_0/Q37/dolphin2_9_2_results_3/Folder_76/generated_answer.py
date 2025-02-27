def filter_chars(s):
    for i in range(379, 899):
        c = s[i]
        if 'M' <= c and c <= 'v':
            s = s[:i] + s[i + 1:]
    return s