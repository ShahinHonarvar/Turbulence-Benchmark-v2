def filter_chars(s):
    for i in range(36, 80):
        if 'a' <= s[i] <= 'i':
            s = s[:i] + s[i + 1:]
    return s