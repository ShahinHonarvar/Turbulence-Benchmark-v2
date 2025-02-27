def filter_chars(s):
    for i in range(124, 855):
        if '9' <= s[i] <= 's':
            return s[:i] + s[i + 1:]
    return s