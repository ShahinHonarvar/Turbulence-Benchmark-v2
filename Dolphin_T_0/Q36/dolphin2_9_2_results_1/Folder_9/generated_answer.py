def filter_chars(s):
    for c in range(50, 92):
        if 'A' < s[c] < 'Q':
            s = s[:c] + s[c + 1:]
    return s