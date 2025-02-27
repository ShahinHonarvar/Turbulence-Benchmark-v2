def filter_chars(s):
    for i in range(12, 89):
        if i < len(s) and '&' <= s[i] <= 'v':
            c = s[i]
            s = s.replace(c, '')
    return s