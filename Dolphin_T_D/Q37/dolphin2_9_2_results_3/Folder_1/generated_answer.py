def filter_chars(s):
    for i in range(41, 80):
        if 'f' <= s[i] <= '|':
            s = s[:i] + s[i + 1:]
    return s