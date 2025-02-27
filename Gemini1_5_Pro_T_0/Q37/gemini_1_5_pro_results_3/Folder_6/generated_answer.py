def filter_chars(s):
    for i in range(13, 29):
        if i < len(s) and 'c' <= s[i] <= 'n':
            c = s[i]
            s = s.replace(c, '')
    return s