def filter_chars(s):
    for i in range(502, 946):
        if i < len(s) and 'W' < s[i] < 'y':
            c = s[i]
            s = s.replace(c, '')
    return s