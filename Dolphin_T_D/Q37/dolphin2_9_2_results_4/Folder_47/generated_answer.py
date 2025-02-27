def filter_chars(s):
    for c in range(38, 55):
        if ':' <= s[c] <= 'r':
            s = s[:c] + s[c + 1:]
    return s