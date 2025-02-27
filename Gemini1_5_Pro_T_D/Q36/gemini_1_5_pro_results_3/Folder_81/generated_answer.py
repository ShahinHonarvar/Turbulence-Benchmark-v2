def filter_chars(s):
    for i in range(52, 76):
        if i < len(s) and '5' < s[i] < 'f':
            c = s[i]
            s = s.replace(c, '')
    return s