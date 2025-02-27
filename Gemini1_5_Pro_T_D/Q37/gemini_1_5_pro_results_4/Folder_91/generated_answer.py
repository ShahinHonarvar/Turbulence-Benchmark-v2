def filter_chars(s):
    for i in range(7, 9):
        if i < len(s) and 'B' <= s[i] <= 'H':
            s = s.replace(s[i], '')
    return s