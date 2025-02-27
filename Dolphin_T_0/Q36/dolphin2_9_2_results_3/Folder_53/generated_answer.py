def filter_chars(s):
    to_remove = []
    for i in range(90, 97):
        if s[i] > 'j' and s[i] < 'w':
            to_remove.append(s[i])
    for c in to_remove:
        s = s.replace(c, '')
    return s