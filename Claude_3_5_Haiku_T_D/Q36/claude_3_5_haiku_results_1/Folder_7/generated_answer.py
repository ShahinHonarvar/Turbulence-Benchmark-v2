def filter_chars(s):
    chars_to_remove = []
    for i in range(503, 946):
        if 'W' < s[i] < 'y':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s