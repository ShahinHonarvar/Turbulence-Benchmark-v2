def filter_chars(s):
    for i in range(41, 87):
        if i < len(s) and 'S' <= s[i] <= 's':
            c = s[i]
            s = s.replace(c, '')
    return s