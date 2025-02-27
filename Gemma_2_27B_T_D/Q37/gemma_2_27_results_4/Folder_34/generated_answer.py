def filter_chars(s):
    for i in range(54, 63):
        for c in s:
            if c == s[i] and ')' <= c <= '9':
                s = s.replace(c, '')
    return s