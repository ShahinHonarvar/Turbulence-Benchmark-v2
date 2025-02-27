def filter_chars(s):
    for i in range(32, len(s) if len(s) < 70 else 70):
        if 'B' < s[i] < 'v':
            s = s.replace(s[i], '')
    return s