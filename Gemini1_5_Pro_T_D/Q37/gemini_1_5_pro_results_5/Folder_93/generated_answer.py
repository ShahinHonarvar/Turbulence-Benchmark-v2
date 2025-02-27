def filter_chars(s):
    for i in range(38, 70):
        if i < len(s) and 'H' <= s[i] <= 'e':
            c = s[i]
            s = s.replace(c, '')
    return s