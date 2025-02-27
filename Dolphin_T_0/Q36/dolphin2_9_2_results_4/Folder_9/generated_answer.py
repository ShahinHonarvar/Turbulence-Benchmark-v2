def filter_chars(s):
    for i in range(50, 92):
        if 'A' < s[i] < 'Q':
            s = s[:i] + s[i + 1:]
    return s