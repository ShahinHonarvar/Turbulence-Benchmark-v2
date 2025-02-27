def filter_chars(s):
    to_remove = []
    for i in range(7, 10):
        if i < len(s) and '6' <= s[i] <= 'w':
            to_remove.append(s[i])
    for c in to_remove:
        s = s.replace(c, '')
    return s