def filter_chars(s):
    for i in range(43, 69):
        order = s[:i]
        if 'A' < s[i] < 'r':
            s = order + s[i + 1:]
    return s