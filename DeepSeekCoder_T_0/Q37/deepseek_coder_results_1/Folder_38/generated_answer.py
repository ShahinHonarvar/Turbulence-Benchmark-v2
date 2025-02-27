def filter_chars(s):
    for i in range(24, 80):
        if 'a' <= s[i] <= 'f':
            s = s.replace(s[i], '')
    return s