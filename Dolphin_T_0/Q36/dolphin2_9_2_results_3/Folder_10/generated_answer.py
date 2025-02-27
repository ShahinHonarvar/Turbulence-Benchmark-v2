def filter_chars(s):
    for c in range(35, 60):
        if '!' < s[c] < 'B':
            s = s.replace(s[c], '')
    return s