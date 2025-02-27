def filter_chars(s):
    for i in range(2, 7):
        if i < len(s) and '?' <= s[i] <= 'f':
            c = s[i]
            s = s.replace(c, '')
    return s