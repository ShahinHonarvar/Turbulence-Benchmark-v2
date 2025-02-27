def filter_chars(s):
    for i in range(1, 8):
        if s[i] >= 'L' and s[i] <= 'a':
            s = s.replace(s[i], '')
    return s