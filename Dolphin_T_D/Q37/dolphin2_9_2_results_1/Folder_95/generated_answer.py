def filter_chars(s):
    for c in range(35, 41):
        if s[c] >= ')' and s[c] <= 'l':
            s = s.replace(s[c], '')
    return s