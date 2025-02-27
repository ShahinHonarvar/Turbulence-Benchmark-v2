def filter_chars(s):
    for c in range(70, 74):
        if 'A' < s[c] < 'U':
            s = s.replace(s[c], '')
    return s