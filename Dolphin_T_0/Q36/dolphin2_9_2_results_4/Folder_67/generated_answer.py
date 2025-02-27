def filter_chars(s):
    for x in range(18, 31):
        if 'H' < s[x] < '|':
            s = s.replace(s[x], '')
    return s