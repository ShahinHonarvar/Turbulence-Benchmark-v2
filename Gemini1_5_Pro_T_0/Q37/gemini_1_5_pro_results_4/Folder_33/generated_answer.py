def filter_chars(s):
    for i in range(722, 833):
        if i < len(s) and 'K' <= s[i] <= 'm':
            c = s[i]
            s = s.replace(c, '')
    return s