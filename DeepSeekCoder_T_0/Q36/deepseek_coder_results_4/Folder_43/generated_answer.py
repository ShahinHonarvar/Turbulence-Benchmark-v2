def filter_chars(s):
    for i in range(28, 75):
        if 'A' < s[i] < 'i':
            s = s.replace(s[i], '')
    return s