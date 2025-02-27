def filter_chars(s):
    for i in range(37, 57):
        if i < len(s) and '6' <= s[i] <= '_':
            c = s[i]
            s = s.replace(c, '')
    return s