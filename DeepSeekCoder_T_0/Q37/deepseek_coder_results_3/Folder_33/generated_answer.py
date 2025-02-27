def filter_chars(s):
    for i in range(722, 833):
        if 'K' <= s[i] <= 'm':
            s = s.replace(s[i], '')
    return s