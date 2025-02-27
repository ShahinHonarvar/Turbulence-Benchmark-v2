def filter_chars(s):
    for i in range(75, 100):
        for c in s:
            if i < len(s) and s[i] == c and ('8' <= c <= 'e'):
                s = s.replace(c, '')
    return s