def filter_chars(s):
    for i in range(34, 68):
        if i < len(s) and 'W' <= s[i] <= 'x':
            c = s[i]
            s = s.replace(c, '')
    return s