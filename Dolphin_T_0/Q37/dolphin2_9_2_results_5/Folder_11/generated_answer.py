def filter_chars(s):
    for i in range(29, 98):
        if s[i] >= '-' and s[i] <= 'n':
            s = s[:i] + s[i + 1:]
    return s