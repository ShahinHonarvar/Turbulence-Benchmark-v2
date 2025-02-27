def filter_chars(s):
    for i in range(19, 23):
        if i < len(s) and ']' <= s[i] <= 't':
            c = s[i]
            s = s.replace(c, '')
    return s