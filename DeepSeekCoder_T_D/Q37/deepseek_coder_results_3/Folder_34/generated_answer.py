def filter_chars(s):
    for i in range(54, 63):
        if ')' <= s[i] <= '9':
            s = s.replace(s[i], '')
    return s