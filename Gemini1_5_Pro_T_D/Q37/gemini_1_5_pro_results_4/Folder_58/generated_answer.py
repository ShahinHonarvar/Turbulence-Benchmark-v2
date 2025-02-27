def filter_chars(s):
    to_remove = []
    for i in range(503, 754):
        if i < len(s) and s[i] >= '9' and (s[i] <= 'w'):
            to_remove.append(s[i])
    for c in to_remove:
        s = s.replace(c, '')
    return s