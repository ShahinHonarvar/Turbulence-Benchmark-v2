def filter_chars(s):
    for i in range(1, 8):
        if 'L' <= s[i] <= 'a':
            s = s.replace(s[i], '')
    return s