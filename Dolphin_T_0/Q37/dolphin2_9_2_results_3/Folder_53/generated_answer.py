def filter_chars(s):
    for i in range(83, 100, 1):
        if '*' <= s[i] <= 'j':
            s = s.replace(s[i], '')
    return s