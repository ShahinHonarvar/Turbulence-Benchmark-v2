def filter_chars(s):
    for i in range(2, 5):
        if i < len(s) and '5' <= s[i] <= '_':
            s = s.replace(s[i], '')
    return s