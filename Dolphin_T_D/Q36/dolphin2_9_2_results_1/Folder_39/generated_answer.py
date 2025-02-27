def filter_chars(s):
    for c in range(43, 59):
        if s[c] > '5' and s[c] < 'C':
            s = ''.join([x for x in s if x != s[c]])
    return s