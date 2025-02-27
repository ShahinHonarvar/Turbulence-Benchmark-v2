def filter_chars(s):
    for i in range(10, 53):
        if i < len(s) and '@' <= s[i] <= 'T':
            c = s[i]
            s = s.replace(c, '')
    return s