def filter_chars(s):
    for i in range(15, 85):
        if i < len(s) and 'I' < s[i] < 'M':
            c = s[i]
            s = s.replace(c, '')
    return s