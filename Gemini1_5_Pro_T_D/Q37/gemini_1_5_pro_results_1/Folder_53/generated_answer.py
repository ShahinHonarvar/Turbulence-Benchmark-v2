def filter_chars(s):
    for i in range(83, 100):
        if i < len(s) and '*' <= s[i] <= 'j':
            c = s[i]
            s = s.replace(c, '')
    return s