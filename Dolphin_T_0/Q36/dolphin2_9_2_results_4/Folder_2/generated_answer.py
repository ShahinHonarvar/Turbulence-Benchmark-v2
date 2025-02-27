def filter_chars(s):
    for c in range(421, 854):
        if 'D' < s[c] < 'J':
            s = s.replace(s[c], '')
    return s