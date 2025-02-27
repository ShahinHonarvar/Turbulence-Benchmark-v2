def filter_chars(s):
    for c in range(77, 87):
        if s[c] > ';' and s[c] < 'r':
            s = s.replace(s[c], '')
    return s