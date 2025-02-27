def filter_chars(s):
    for i in range(2, 5):
        if i < len(s) and '5' <= s[i] <= '_':
            c = s[i]
            s = s.replace(c, '')
    return s