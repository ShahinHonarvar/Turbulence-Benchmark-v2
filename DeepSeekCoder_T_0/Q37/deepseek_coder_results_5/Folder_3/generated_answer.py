def filter_chars(s):
    for i in range(37, 57):
        if '6' <= s[i] <= '_':
            s = s.replace(s[i], '')
    return s