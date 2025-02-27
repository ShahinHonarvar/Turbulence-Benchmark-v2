def filter_chars(s):
    to_remove = []
    for i in range(41, 56):
        if 'Z' < s[i] < 'c':
            to_remove.append(s[i])
    for r in to_remove:
        s = s.replace(r, '')
    return s