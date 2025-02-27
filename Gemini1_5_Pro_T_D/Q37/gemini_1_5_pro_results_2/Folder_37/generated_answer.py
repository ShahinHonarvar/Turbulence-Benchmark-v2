def filter_chars(s):
    for i in range(17, 64):
        if i < len(s) and 'O' <= s[i] <= '^':
            c = s[i]
            s = s.replace(c, '')
    return s