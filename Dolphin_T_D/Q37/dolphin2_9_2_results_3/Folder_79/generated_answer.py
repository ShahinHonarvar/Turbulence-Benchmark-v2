def filter_chars(s):
    for i in range(10, 53):
        if s[i] >= '@' and s[i] <= 'T':
            s = s[:i] + s[i + 1:]
    return s