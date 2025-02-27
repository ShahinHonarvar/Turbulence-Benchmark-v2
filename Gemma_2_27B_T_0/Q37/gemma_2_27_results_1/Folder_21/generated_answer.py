def filter_chars(s):
    for i in range(603, 760):
        if i < len(s) and s[i] >= 'Q' and (s[i] <= 'h'):
            s = s.replace(s[i], '')
    return s