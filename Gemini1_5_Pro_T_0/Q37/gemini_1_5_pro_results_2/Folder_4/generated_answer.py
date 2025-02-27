def filter_chars(s):
    for i in range(19, 34):
        if i < len(s) and 'S' <= s[i] <= '{':
            c = s[i]
            s = s.replace(c, '')
    return s