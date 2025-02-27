def filter_chars(s):
    for i in range(35, 60):
        if i < len(s) and '!' < s[i] < 'B':
            c = s[i]
            s = s.replace(c, '')
    return s