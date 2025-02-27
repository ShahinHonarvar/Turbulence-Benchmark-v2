def filter_chars(s):
    for i in range(225, 382):
        if 'D' <= s[i] <= 'Y':
            s = s[:i] + s[i + 1:]
    return s