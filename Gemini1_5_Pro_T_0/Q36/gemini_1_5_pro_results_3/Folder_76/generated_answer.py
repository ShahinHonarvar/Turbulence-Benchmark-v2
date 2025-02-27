def filter_chars(s):
    for i in range(669, 888):
        if i < len(s) and 'B' < s[i] < 'Y':
            c = s[i]
            s = s.replace(c, '')
    return s