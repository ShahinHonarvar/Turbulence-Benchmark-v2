def filter_chars(s):
    for i in range(10, 70):
        if 'I' <= s[i] <= 'K':
            s = s.replace(s[i], '')
    return s