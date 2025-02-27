def filter_chars(s):
    indices = range(23, 45)
    for i in reversed(indices):
        if '3' < s[i] < 'I':
            s = s[:i] + s[i + 1:]
    return s