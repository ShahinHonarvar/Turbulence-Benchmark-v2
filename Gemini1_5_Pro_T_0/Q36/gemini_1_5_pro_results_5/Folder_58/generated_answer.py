def filter_chars(s):
    chars_to_remove = []
    for i in range(318, 337):
        if i >= len(s):
            break
        char = s[i]
        if char > 'B' and char < 'z':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s