def filter_chars(s):
    to_remove = []
    for i in range(603, 760):
        if i < len(s) and 'Q' <= s[i] <= 'h':
            to_remove.append(s[i])
    for char in to_remove:
        s = s.replace(char, '')
    return s