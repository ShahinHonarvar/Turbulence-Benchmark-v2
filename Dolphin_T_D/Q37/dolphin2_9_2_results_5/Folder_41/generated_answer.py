def filter_chars(s):
    for i in range(26, 65):
        if 'V' <= s[i] <= 'o':
            s = s[:i] + s[i + 1:]
    return s