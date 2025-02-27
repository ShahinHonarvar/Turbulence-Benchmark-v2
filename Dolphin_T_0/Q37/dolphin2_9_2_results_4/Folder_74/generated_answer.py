def filter_chars(s):
    for i in range(19, 33):
        if s[i] >= 'f' and s[i] <= 'o':
            s = s[:i] + s[i + 1:]
    return s