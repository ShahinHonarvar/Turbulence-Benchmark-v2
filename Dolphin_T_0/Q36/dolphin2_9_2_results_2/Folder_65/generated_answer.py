def filter_chars(s):
    for c in range(58, 82):
        if 'F' < s[c] < 'O':
            s = s.replace(s[c], '')
    return s