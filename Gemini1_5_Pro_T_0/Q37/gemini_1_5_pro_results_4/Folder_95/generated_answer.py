def filter_chars(s):
    for i in range(35, 41):
        if i < len(s) and ')' <= s[i] <= 'l':
            c = s[i]
            s = s.replace(c, '')
    return s