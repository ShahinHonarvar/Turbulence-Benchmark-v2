def filter_chars(s):
    for i in range(24, 83):
        if s[i] >= '5' and s[i] <= '<':
            s = s[:i] + s[i + 1:]
    return s