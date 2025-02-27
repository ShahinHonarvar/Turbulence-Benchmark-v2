def filter_chars(s):
    for i in range(42, 93):
        if '/' <= s[i] <= 'a':
            s = s.replace(s[i], '')
    return s