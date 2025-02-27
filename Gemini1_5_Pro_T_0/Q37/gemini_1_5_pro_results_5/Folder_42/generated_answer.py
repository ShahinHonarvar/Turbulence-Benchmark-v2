def filter_chars(s):
    for i in range(73, 75):
        if i < len(s) and 'U' <= s[i] <= 'l':
            c = s[i]
            s = s.replace(c, '')
    return s