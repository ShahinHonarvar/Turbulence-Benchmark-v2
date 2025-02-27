def filter_chars(s):
    for c in range(10, 15):
        if 't' < s[c] < 'v':
            s = s.replace(s[c], '')
    return s