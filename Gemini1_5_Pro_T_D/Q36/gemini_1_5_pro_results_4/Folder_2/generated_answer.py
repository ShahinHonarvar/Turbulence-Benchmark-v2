def filter_chars(s):
    chars_to_remove = []
    for i in range(421, 854):
        char = s[i]
        if char > 'D' and char < 'J':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s