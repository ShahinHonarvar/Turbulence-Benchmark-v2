def filter_chars(s):
    for c in range(19, 23):
        if ']' <= s[c] <= 't':
            s = s[:c] + s[c + 1:]
    return s