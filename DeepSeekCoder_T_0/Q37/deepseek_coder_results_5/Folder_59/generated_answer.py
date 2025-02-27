def filter_chars(s):
    for i in range(2, 4):
        if '5' <= s[i] <= '_':
            s = s.replace(s[i], '')
    return s