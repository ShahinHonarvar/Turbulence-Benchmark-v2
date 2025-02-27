def filter_chars(s):
    for i in range(52, 82):
        if 'A' <= s[i] <= 'U':
            s = s.replace(s[i], '')
    return s