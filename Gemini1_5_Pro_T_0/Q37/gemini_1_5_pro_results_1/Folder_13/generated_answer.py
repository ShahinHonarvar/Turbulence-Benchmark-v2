def filter_chars(s):
    for i in range(124, 855):
        if i < len(s) and '9' <= s[i] <= 's':
            c = s[i]
            s = s.replace(c, '')
    return s