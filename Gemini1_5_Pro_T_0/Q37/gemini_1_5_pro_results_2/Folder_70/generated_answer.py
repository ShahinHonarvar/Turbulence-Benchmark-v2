def filter_chars(s):
    for i in range(515, 539):
        if i < len(s) and '+' <= s[i] <= '}':
            c = s[i]
            s = s.replace(c, '')
    return s