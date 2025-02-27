def filter_chars(s):
    for c in range(18, 95):
        if s[c] > 'K' and s[c] < 'a':
            s = s.replace(s[c], '')
    return s