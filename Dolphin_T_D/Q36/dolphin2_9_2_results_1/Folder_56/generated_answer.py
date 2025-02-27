def filter_chars(s):
    for i in range(31, 50):
        c = s[i]
        if c > '/' and c < 'J':
            s = s[:i] + s[i + 1:]
    return s