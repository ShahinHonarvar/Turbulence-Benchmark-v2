def filter_chars(s):
    for i in range(225, 382):
        if 'D' <= s[i] <= 'Y':
            s = s.replace(s[i], '')
    return s