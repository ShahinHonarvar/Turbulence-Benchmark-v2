def filter_chars(s):
    for i in range(310, 591):
        if s[i] > 'S' and s[i] < 'm':
            s = s.replace(s[i], '')
    return s