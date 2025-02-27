def filter_chars(s):
    for i in range(19, 31):
        if s[i] > 'H' and s[i] < '|':
            s = s.replace(s[i], '')
    return s