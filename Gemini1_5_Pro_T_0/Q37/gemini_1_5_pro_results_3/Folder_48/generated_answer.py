def filter_chars(s):
    for i in range(513, 878):
        if i < len(s) and '?' <= s[i] <= 'n':
            c = s[i]
            s = s.replace(c, '')
    return s