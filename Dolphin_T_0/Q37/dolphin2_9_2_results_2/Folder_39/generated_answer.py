def filter_chars(s):
    for c in range(52, 82):
        if 'A' <= s[c] <= 'U':
            s = s[:c] + s[c + 1:]
    return s