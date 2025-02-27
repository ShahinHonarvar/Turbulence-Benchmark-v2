def filter_chars(s):
    for i in range(71, 95):
        if 'K' <= s[i] <= 'a':
            s = s.replace(s[i], '')
    return s