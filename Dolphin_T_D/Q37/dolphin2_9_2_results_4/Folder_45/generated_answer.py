def filter_chars(s):
    chars_to_remove = []
    for i in range(72, 95):
        if s[i] >= '.' and s[i] <= 'b':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s