def filter_chars(s):
    for i in range(24, 80):
        if s[i] >= 'a' and s[i] <= 'f':
            s = s[:i] + s[i + 1:]
    return s