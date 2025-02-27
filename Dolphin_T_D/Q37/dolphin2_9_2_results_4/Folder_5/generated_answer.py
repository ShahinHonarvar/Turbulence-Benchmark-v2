def filter_chars(s):
    for c in range(24, 83):
        if s[c] >= '5' and s[c] <= '<':
            s = s.replace(s[c], '')
    return s