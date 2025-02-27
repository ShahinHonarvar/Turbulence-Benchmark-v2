def filter_chars(s):
    for i in range(114, 640):
        if s[i] >= '!' and s[i] <= 'x':
            s = s[:i] + s[i + 1:]
    return s