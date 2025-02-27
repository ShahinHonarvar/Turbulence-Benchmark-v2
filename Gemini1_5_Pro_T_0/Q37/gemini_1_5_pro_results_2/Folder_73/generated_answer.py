def filter_chars(s):
    for i in range(22, 86):
        if i < len(s) and '7' <= s[i] <= 'e':
            c = s[i]
            s = s.replace(c, '')
    return s