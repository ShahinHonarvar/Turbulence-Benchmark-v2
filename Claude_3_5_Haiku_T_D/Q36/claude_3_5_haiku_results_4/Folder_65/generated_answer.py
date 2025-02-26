def filter_chars(s):
    chars_to_remove = []
    for i in range(59, 82):
        if 'F' < s[i] < 'O':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s