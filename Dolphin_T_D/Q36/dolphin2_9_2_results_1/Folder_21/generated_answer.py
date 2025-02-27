def filter_chars(s):
    for c in range(219, 403):
        if s[c] > '*' and s[c] < '7':
            s = s.replace(s[c], '')
    return s