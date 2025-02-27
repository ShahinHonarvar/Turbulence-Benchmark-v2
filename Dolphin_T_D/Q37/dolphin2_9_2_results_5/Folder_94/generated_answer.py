def filter_chars(s):
    for i in range(51, 97):
        if s[i] >= 'X' and s[i] <= 'p':
            s = s[:i] + s[i + 1:]
    return s