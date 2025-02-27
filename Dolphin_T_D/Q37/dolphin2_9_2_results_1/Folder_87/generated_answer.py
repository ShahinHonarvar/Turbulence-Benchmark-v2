def filter_chars(s):
    for c in range(18, 82):
        if s[c] >= 'W' and s[c] <= '[':
            s = s[:c] + s[c + 1:]
    return s