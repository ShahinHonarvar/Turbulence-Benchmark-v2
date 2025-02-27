def filter_chars(s):
    for i in range(72, 95):
        if '.' <= s[i] <= 'b':
            s = s.replace(s[i], '')
    return s