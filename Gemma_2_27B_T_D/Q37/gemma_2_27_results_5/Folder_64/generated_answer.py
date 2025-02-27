def filter_chars(s):
    for i in range(1, 8):
        for c in s[i]:
            if 'L' <= c <= 'a':
                s = s.replace(c, '')
    return s