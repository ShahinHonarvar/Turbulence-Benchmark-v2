def filter_chars(s):
    for i in range(43, 81):
        if '=' <= s[i] <= 'E':
            s = s[:i] + s[i + 1:]
    return s