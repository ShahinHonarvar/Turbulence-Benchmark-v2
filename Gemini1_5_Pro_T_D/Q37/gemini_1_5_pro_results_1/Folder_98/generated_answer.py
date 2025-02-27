def filter_chars(s):
    for i in range(8, 10):
        if i < len(s) and 'R' <= s[i] <= 't':
            s = s.replace(s[i], '')
    return s