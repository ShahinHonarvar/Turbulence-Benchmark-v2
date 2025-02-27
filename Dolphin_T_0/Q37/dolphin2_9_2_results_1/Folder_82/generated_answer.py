def filter_chars(s):
    for i in range(12, 26):
        if s[i] >= 'P' and s[i] <= 'x':
            s = s.replace(s[i], '')
    return s