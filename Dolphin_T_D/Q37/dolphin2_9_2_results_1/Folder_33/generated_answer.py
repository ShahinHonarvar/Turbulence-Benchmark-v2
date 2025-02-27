def filter_chars(s):
    for c in range(722, 833):
        if s[c] >= 'K' and s[c] <= 'm':
            s = s[:c] + s[c + 1:]
    return s