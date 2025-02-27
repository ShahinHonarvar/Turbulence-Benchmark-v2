def filter_chars(s):
    for c in range(51, 76):
        if '5' < s[c] < 'f':
            s = ''.join([x for x in s if x != s[c]])
    return s