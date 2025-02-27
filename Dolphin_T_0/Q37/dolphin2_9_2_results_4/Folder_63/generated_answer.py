def filter_chars(s):
    for i in range(42, 93):
        ch = s[i]
        if ch >= '/' and ch <= 'a':
            s = s[:i] + s[i + 1:]
    return s