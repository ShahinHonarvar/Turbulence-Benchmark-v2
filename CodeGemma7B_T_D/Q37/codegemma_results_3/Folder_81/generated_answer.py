def filter_chars(s):
    for i in range(19, 93):
        while s[i] >= '8' and s[i] <= 'm':
            s = s[:i] + s[i + 1:]
    return s