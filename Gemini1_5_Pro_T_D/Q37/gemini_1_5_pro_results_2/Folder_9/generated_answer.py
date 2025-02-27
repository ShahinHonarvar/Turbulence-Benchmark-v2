def filter_chars(s):
    for i in range(38, 100):
        if i < len(s) and 'A' <= s[i] <= 'Q':
            c = s[i]
            s = s.replace(c, '')
    return s