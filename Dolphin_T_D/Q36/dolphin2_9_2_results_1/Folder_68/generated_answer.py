def filter_chars(s):
    for c in range(1, 9):
        if '8' < s[c] < 'm':
            s = s.replace(s[c], '')
    return s