def filter_chars(s):
    for c in range(41, 87):
        if s[c] >= 'S' and s[c] <= 's':
            s = s.replace(s[c], '')
    return s