def filter_chars(s):
    chars_to_remove = []
    for i in range(57, 86):
        if '+' < s[i] < 'w':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s