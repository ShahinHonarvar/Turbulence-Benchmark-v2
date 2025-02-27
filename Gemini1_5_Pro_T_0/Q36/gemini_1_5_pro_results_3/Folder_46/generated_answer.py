def filter_chars(s):
    for i in range(19, 69):
        if i < len(s) and s[i] > '<' and (s[i] < 'C'):
            c = s[i]
            s = s.replace(c, '')
    return s