def filter_chars(s):
    for i in range(331, 713):
        if i < len(s) and 'M' < s[i] < '_':
            c = s[i]
            s = s.replace(c, '')
    return s