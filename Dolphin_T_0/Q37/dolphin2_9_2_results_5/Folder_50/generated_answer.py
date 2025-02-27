def filter_chars(s):
    for i in range(71, 97):
        if s[i] >= '_' and s[i] <= 'o':
            s = s[:i] + s[i + 1:]
    return s