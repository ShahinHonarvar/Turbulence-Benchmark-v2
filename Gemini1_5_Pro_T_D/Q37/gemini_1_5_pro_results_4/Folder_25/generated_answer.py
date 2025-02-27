def filter_chars(s):
    for i in range(31, 39):
        if i < len(s) and ';' <= s[i] <= 'g':
            c = s[i]
            s = s.replace(c, '')
    return s