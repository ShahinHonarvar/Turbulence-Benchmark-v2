def filter_chars(s):
    for i in range(83, 100):
        if '*' <= s[i] <= 'j':
            s = s.replace(s[i], '')
    return s