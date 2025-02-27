def filter_chars(s):
    for i in range(86, 93):
        if i < len(s) and '!' <= s[i] <= 's':
            c = s[i]
            s = s.replace(c, '')
    return s