def filter_chars(s):
    for i in range(75, 100):
        if i < len(s) and '8' <= s[i] <= 'e':
            c = s[i]
            s = s.replace(c, '')
    return s