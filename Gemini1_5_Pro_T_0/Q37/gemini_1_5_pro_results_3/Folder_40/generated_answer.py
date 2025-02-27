def filter_chars(s):
    for i in range(2):
        if i < len(s) and '*' <= s[i] <= 's':
            c = s[i]
            s = s.replace(c, '')
    return s