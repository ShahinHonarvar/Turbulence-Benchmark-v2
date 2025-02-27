def filter_chars(s):
    for i in range(42, 78):
        if i < len(s) and '!' < s[i] < '?':
            c = s[i]
            s = s.replace(c, '')
    return s