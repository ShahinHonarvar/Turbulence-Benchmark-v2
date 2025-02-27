def filter_chars(s):
    for i in range(71, 97):
        c = s[i]
        if c >= '_' and c <= 'o':
            s = s[:i] + s[i + 1:]
    return s