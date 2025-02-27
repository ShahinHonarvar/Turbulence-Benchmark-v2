def filter_chars(s):
    for i in range(30, 33):
        if i < len(s) and '%' < s[i] < 'a':
            c = s[i]
            s = s.replace(c, '')
    return s