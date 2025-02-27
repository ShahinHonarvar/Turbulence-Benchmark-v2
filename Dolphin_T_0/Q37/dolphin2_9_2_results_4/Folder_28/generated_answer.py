def filter_chars(s):
    for i in range(20, 80):
        if s[i] >= '!' and s[i] <= 'T':
            s = s[:i] + s[i + 1:]
    return s