def filter_chars(s):
    for i in range(42, 93):
        if '/' <= s[i] <= 'a':
            s = s[:i] + s[i + 1:]
    return s