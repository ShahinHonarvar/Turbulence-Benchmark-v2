def filter_chars(s):
    for i in range(10, 70):
        if i < len(s) and s[i] >= 'I' and (s[i] <= 'K'):
            c = s[i]
            s = s.replace(c, '')
    return s