def filter_chars(s):
    to_remove = []
    for i in range(75, 100):
        if i < len(s) and '8' <= s[i] <= 'e':
            to_remove.append(s[i])
    for c in to_remove:
        s = s.replace(c, '')
    return s