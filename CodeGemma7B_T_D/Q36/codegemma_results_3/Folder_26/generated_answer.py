def filter_chars(s):
    for i in range(43, 83):
        if s[i] > ':' and s[i] < 'Q':
            s = s[:i] + s[i + 1:]
    return s