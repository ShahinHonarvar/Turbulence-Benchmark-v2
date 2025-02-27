def filter_chars(s):
    for c in range(12, 89):
        if '&' <= s[c] <= 'v':
            s = s[:c] + s[c + 1:]
    return s