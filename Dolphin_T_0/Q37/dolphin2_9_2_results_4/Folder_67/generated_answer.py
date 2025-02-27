def filter_chars(s):
    for i in range(19, 23):
        if ']' <= s[i] <= 't':
            s = s[:i] + s[i + 1:]
    return s