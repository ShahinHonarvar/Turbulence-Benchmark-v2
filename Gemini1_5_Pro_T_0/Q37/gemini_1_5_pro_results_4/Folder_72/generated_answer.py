def filter_chars(s):
    for i in range(35, 52):
        if i < len(s) and 'H' <= s[i] <= 's':
            c = s[i]
            s = s.replace(c, '')
    return s