def filter_chars(s):
    for i in range(35, 41):
        if ')' <= s[i] <= 'l':
            s = s[:i] + s[i + 1:]
    return s