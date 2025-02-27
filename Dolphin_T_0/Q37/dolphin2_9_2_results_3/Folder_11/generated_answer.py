def filter_chars(s):
    for c in range(29, 98):
        if 'ð\x9d\x92\x82' <= s[c] <= 'n':
            s = s[:c] + s[c + 1:]
    return s