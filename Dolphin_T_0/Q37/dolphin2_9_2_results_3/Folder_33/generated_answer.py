def filter_chars(s):
    for i in range(722, 833):
        if s[i] >= 'K' and s[i] <= 'm':
            s = s.replace(s[i], '')
    return s