def filter_chars(s):
    for i in range(19, 34):
        if i <= len(s) - 1:
            if s[i] >= 'S' and s[i] <= '{':
                c = s[i]
                s = s.replace(c, '')
    return s