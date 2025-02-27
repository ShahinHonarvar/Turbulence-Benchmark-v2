def filter_chars(s):
    for i in range(4, 5):
        if '7' <= s[i] <= 'o':
            s = s.replace(s[i], '')
    return s