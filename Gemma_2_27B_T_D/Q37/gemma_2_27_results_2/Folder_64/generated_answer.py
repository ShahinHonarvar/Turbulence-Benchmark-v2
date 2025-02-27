def filter_chars(s):
    for i in range(1, 8):
        if len(s) > i and 'L' <= s[i] <= 'a':
            s = s.replace(s[i], '')
    return s