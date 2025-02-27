def filter_chars(s):
    for c in range(55, 66):
        if 'f' < s[c] < '|':
            s = ''.join([x for x in s if x != s[c]])
    return s