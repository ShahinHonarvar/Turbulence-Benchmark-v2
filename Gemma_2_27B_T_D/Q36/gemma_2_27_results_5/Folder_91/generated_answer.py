def filter_chars(s):
    for i in range(0, 3):
        if s[i] > '$' and s[i] < '?':
            s = s.replace(s[i], '')
    return s