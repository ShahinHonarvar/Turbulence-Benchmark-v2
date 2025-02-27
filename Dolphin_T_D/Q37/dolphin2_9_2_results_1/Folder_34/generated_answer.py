def filter_chars(s):
    for i in range(54, 63):
        c = s[i]
        if c >= ')' and c <= '9':
            s = s.replace(c, '')
    return s