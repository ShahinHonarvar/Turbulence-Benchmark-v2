def filter_chars(s):
    for c in range(18, 64):
        if '3' < s[c] < 'B':
            s = s.replace(s[c], '')
    return s