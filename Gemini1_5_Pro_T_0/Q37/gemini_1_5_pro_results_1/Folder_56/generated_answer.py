def filter_chars(s):
    for i in range(71, 95):
        if i < len(s) and 'K' <= s[i] <= 'a':
            c = s[i]
            s = s.replace(c, '')
    return s