def filter_chars(s):
    for c in range(61, 88):
        if s[c] > '%' and s[c] < 'q':
            s = s.replace(s[c], '')
    return s