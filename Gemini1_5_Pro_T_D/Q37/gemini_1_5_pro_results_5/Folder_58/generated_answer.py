def filter_chars(s):
    to_remove = []
    for i in range(503, 754):
        if i < len(s) and '9' <= s[i] <= 'w':
            to_remove.append(s[i])
    for char in to_remove:
        s = s.replace(char, '')
    return s