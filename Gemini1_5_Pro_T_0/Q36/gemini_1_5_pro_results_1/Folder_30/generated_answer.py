def filter_chars(s):
    for i in range(24, 45):
        if i < len(s) and '3' < s[i] < 'I':
            c = s[i]
            s = s.replace(c, '')
    return s