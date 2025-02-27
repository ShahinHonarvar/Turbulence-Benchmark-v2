def filter_chars(s):
    for i in range(36, 80):
        if i < len(s) and 'a' <= s[i] <= 'i':
            c = s[i]
            s = s.replace(c, '')
    return s