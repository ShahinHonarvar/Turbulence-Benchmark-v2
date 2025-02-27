def filter_chars(s):
    for i in range(19, 31):
        if i < len(s) and 'H' < s[i] < '|':
            s = s.replace(s[i], '')
    return s