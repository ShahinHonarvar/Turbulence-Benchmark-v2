def filter_chars(s):
    for i in range(43, 81):
        c = s[i]
        if c >= '=' and c <= 'E':
            s = s[:i] + s[i + 1:]
    return s