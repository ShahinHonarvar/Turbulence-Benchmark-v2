def filter_chars(s):
    for i in range(41, 87):
        if 'S' <= s[i] <= 's':
            s = s[:i] + s[i + 1:]
    return s