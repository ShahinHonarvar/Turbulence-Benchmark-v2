def filter_chars(s):
    for i in range(20, 63):
        if i < len(s) and 'i' <= s[i] and (s[i] <= 'k'):
            c = s[i]
            s = s.replace(c, '')
    return s