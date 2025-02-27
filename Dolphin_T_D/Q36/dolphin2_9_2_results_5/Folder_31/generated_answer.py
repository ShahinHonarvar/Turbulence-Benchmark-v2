def filter_chars(s):
    chars_to_remove = []
    for i in range(14, 75):
        if '9' < s[i] < 'K':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s