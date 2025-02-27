def filter_chars(s):
    for i in range(227, 236):
        c = s[i]
        if c >= 'D' and c <= 'u':
            s = s[:i] + s[i + 1:]
    return s