def filter_chars(s):
    for c in range(11, 46):
        if s[c] > '!' and s[c] < 'A':
            s = s.replace(s[c], '')
    return s