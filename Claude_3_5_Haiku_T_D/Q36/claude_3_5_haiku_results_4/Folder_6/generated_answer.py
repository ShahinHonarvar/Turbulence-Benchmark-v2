def filter_chars(s):
    to_remove = []
    for i in range(32, 70):
        if 'B' < s[i] < 'v':
            to_remove.append(s[i])
    for char in to_remove:
        s = s.replace(char, '')
    return s