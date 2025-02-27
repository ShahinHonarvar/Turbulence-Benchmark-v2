def filter_chars(s):
    for c in range(51, 76):
        if s[c] > '5' and s[c] < 'f':
            return s.replace(s[c], '')
    return s