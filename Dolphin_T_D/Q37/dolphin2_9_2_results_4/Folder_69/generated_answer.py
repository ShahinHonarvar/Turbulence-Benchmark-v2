def filter_chars(s):
    for i in range(114, 640):
        c = s[i]
        if c >= '!' and c <= 'x':
            s = s[:i] + s[i + 1:]
    return s