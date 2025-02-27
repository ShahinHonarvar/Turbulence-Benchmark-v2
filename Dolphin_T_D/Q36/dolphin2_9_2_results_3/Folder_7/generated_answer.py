def filter_chars(s):
    for c in range(502, 946):
        ch = s[c]
        if 'W' < ch < 'y':
            s = s[:c] + s[c + 1:]
    return s