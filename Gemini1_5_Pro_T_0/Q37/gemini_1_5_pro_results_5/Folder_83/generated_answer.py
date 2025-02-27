def filter_chars(s):
    for i in range(29, 80):
        if i < len(s) and 'K' <= s[i] <= 'z':
            c = s[i]
            s = s.replace(c, '')
    return s