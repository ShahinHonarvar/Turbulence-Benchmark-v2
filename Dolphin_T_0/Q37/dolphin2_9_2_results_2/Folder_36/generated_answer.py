def filter_chars(s):
    for i in range(259, 503):
        if s[i] >= ',' and s[i] <= '3':
            s = s[:i] + s[i + 1:]
    return s