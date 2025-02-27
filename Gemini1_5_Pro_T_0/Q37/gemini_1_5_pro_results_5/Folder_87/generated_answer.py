def filter_chars(s):
    for i in range(18, 82):
        if i < len(s) and s[i] >= 'W' and (s[i] <= '['):
            c = s[i]
            s = s.replace(c, '')
    return s