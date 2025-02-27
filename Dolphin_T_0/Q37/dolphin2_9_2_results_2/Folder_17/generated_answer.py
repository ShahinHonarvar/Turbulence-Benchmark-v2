def filter_chars(s):
    for i in range(27, 30):
        c = s[i]
        if not ';' <= c <= 'b':
            s = s[:i] + s[i + 1:]
    return s