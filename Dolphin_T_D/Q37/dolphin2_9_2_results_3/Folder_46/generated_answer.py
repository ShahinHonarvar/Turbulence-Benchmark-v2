def filter_chars(s):
    for i in range(11, 73):
        if 'i' <= s[i] <= 'v':
            s = s[:i] + s[i + 1:]
    return s