def filter_chars(s):
    for i in range(384, 412):
        c = s[i]
        if c >= '/' and c <= '8':
            s = s[:i] + s[i + 1:]
    return s