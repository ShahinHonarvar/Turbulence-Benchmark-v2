def filter_chars(s):
    for c in range(32, 39):
        if ';' <= s[c] <= 'g':
            s = s.replace(s[c], '')
    return s