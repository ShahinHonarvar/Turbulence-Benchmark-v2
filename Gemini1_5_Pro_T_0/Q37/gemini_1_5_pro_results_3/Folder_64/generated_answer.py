def filter_chars(s):
    for i in range(1, 8):
        if i < len(s) and 'L' <= s[i] <= 'a':
            s = s.replace(s[i], '')
    return s