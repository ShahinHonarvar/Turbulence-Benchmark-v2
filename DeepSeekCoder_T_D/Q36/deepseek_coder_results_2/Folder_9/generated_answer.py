def filter_chars(s):
    for i in range(51, 92):
        if 'A' < s[i] < 'Q':
            s = s.replace(s[i], '')
    return s