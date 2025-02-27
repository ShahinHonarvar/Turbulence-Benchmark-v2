def filter_chars(s):
    for c in range(587, 648):
        if ',' < s[c] < 'c':
            s = s.replace(s[c], '')
    return s