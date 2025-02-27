def filter_chars(s):
    for i in range(71, 74):
        if i < len(s) and 'A' < s[i] < 'U':
            c = s[i]
            s = s.replace(c, '')
    return s