def filter_chars(s):
    for c in range(69, 87):
        if '#' < s[c] < 'L':
            s = s.replace(s[c], '')
    return s