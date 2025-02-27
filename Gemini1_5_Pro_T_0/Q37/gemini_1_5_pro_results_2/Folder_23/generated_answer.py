def filter_chars(s):
    for i in range(51, 78):
        if i < len(s) and 'V' <= s[i] <= 'Y':
            c = s[i]
            s = s.replace(c, '')
    return s