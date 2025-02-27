def filter_chars(s):
    for i in range(19, 91):
        if s[i] >= 'F' and s[i] <= 'h':
            s = s[:i] + s[i + 1:]
    return s