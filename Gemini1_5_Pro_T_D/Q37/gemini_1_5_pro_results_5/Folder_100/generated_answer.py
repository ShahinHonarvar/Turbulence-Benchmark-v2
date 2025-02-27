def filter_chars(s):
    for i in range(88, 91):
        if i < len(s) and 'J' <= s[i] <= 'Q':
            c = s[i]
            s = s.replace(c, '')
    return s