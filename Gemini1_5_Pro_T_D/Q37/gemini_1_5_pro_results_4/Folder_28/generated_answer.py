def filter_chars(s):
    for i in range(20, 80):
        if i < len(s) and '!' <= s[i] <= 'T':
            c = s[i]
            s = s.replace(c, '')
    return s