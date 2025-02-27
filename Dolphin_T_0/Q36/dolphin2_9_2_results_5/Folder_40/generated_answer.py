def filter_chars(s):
    chars = []
    for i in range(1, 7):
        if s[i] > '-' and s[i] < 'L':
            chars.append(s[i])
    for c in chars:
        s = s.replace(c, '')
    return s