def filter_chars(s):
    for i in range(42, 93):
        if s[i] >= '/' and s[i] <= 'a':
            while s[i] in s:
                s = s[:i] + s[i + 1:]
    return s