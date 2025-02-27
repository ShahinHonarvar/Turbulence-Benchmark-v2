def filter_chars(s):
    for i in range(73, 75):
        if i < len(s) and 'U' <= s[i] <= 'l':
            s = s.replace(s[i], '')
    return s