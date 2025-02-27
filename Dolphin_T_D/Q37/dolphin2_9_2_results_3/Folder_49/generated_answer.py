def filter_chars(s):
    for i in range(42, 98):
        if s[i] >= '*' and s[i] <= 'b':
            s = s[:i] + s[i + 1:]
    return s