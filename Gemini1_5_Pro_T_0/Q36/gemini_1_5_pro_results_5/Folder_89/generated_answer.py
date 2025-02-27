def filter_chars(s):
    chars_to_remove = []
    for i in range(58, 69):
        if s[i] > '(' and s[i] < 'W':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s