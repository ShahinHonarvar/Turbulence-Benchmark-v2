def filter_chars(s):
    for i in range(19, 31):
        if 'H' < s[i] < '|':
            s = s.replace(s[i], '')
    return s