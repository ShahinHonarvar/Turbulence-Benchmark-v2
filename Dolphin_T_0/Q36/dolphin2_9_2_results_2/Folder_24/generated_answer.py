def filter_chars(s):
    for c in range(11, 15):
        if s[c] > 't' and s[c] < 'v':
            s = s.replace(s[c], '')
    return s