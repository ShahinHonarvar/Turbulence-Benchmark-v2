def filter_chars(s):
    for i in range(54, 63):
        if i < len(s) and ')' <= s[i] <= '9':
            c = s[i]
            s = s.replace(c, '')
    return s