def filter_chars(s):
    for i in range(88, 91):
        if 'J' <= s[i] <= 'Q':
            s = s.replace(s[i], '')
    return s