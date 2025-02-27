def filter_chars(s):
    for c in range(41, 56):
        if s[c] > 'Z' and s[c] < 'c':
            s = s.replace(s[c], '')
    return s