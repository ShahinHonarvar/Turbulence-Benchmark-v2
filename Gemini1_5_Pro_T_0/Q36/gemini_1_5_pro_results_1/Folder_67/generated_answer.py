def filter_chars(s):
    for i in range(19, 31):
        if i < len(s) and 'H' < s[i] < '|':
            c = s[i]
            s = s.replace(c, '')
    return s