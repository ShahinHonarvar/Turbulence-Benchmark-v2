def filter_chars(s):
    chars_to_remove = []
    for i in range(27, 75):
        if 'A' < s[i] < 'i':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s