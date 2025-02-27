def filter_chars(s):
    to_remove = []
    for i in range(513, 878):
        if i < len(s) and s[i] >= '?' and (s[i] <= 'n'):
            to_remove.append(s[i])
    for c in to_remove:
        s = s.replace(c, '')
    return s