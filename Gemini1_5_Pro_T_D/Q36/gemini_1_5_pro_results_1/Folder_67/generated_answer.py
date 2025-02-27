def filter_chars(s):
    for i in range(18, 31):
        if i < len(s) and 'H' < s[i] < '|':
            c = s[i]
            s = s.replace(c, '')
    return s