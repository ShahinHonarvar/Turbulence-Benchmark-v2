def filter_chars(s):
    for i in range(32, len(s) - 1 if len(s) < 70 else 69):
        if 'B' < s[i] < 'v':
            s = s.replace(s[i], '')
    return s