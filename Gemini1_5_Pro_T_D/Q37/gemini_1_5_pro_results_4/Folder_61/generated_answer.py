def filter_chars(s):
    to_remove = []
    for i in range(5, 7):
        if i < len(s) and 'G' <= s[i] <= 'p':
            to_remove.append(s[i])
    for c in to_remove:
        s = s.replace(c, '')
    return s