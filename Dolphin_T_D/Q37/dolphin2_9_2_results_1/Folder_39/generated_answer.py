def filter_chars(s):
    for i in range(52, 82):
        if s[i] >= 'A' and s[i] <= 'U':
            s = s.replace(s[i], '')
    return s