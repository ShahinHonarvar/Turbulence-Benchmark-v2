def filter_chars(s):
    for i in range(225, 382):
        if i < len(s) and s[i] >= 'D' and (s[i] <= 'Y'):
            s = s.replace(s[i], '')
    return s