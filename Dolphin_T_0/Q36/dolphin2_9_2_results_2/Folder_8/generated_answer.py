def filter_chars(s):
    for c in range(82, 93):
        if '!' < s[c] < '*':
            s = s.replace(s[c], '')
    return s