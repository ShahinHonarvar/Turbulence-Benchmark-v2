def filter_chars(s):
    for i in range(12, 26):
        if i < len(s) and 'P' <= s[i] <= 'x':
            c = s[i]
            s = s.replace(c, '')
    return s