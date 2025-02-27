def filter_chars(s):
    for i in range(14, 75):
        if s[i] > '9' and s[i] < 'K':
            s = s[:i] + s[i + 1:]
    return s